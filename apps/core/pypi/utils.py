from pypi_slug import getslug
from .models import Project

def get_project_id(name):
    try:
        slug = getslug(name)
        project = Project.objects.get(slug=slug)
        return project.id
    except DoesNotExist:
        pass
