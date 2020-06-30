from django.http import HttpResponse

from apps.core.stdlib.models import Stdlib
from django.views.generic.base import View

STDLIB_NAMES = list(Stdlib.objects.values_list('name',flat=True))

class StdlibView(View):
    def get(self):
        return HttpResponse("\n".join(STDLIB_NAMES))
