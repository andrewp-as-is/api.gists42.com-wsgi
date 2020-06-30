from django.http import HttpResponse
from django.views.generic.base import View
import list_imports

from apps.core.mapping.models import DefaultMapping, UserMapping
from apps.core.pypi.models import Project
from apps.core.stdlib.models import Stdlib
from apps.core.token.models import Token

STDLIB_NAMES = list(Stdlib.objects.values_list('name',flat=True))
DEFAULTMAPPING = {m.name: m.value for m in DefaultMapping.objects.all()}

class RequiresView(View):
    def dispatch(self, *args, **kwargs):
        if 'HTTP_AUTHORIZATION' not in self.request.META:
            return HttpResponse('Unauthorized', status=401)
        try:
            value = self.request.META['HTTP_AUTHORIZATION'].replace('Token ','')
            self.token = Token.objects.get(value=value)
            self.github_user = self.token.created_by
            return super(RequiresView, self).dispatch(*args, **kwargs)
        except Token.DoesNotExist:
            return HttpResponse('Unauthorized', status=401)

    def getnames(self,imports):
        global DEFAULTMAPPING, STDLIB_NAMES
        names = list(set(map(lambda m:m.split('.')[0],imports))-set(STDLIB_NAMES))
        usermapping_data = {}
        usermapping_data = {m.name: m.value for m in UserMapping.objects.filter(
            created_by_id = self.token.created_by
        ).all()}
        for name in names:
            if name in usermapping_data:
                yield usermapping_data[name]
                continue
            if name in DEFAULTMAPPING:
                yield DEFAULTMAPPING[name]
                continue
            yield name

    def getrequirements(self,imports):
        requirements = []
        names = list(filter(None,list(self.getnames(imports))))
        projects = Project.objects.filter(name__in=names).all()
        for project in projects:
            l = '%s==%s' % (project.name,project.version) if project.version else project.name
            requirements.append(l)
        return "\n".join(requirements)

    def post(self, request):
        imports = []
        for basename,_ in request.FILES.items():
            for f in request.FILES.getlist(basename):
                code = f.read().decode("utf-8")
                try:
                    imports+=list(map(lambda m:m.split('.')[0],list_imports.parse(code)))
                except SyntaxError:
                    return HttpResponse('SyntaxError', status=500)
                except Exception as e:
                    return HttpResponse('%s: %s' % (type(e).__name__,str(e)), status=500)
        requirements = self.getrequirements(imports)
        return HttpResponse(requirements, content_type="text/plain")
