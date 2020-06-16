from django.contrib.postgres.search import SearchVectorField
from django.db import models

class Project(models.Model):
    slug = models.TextField(unique=True)
    name = models.TextField(unique=True)
    version = models.TextField(null=True)

    class Meta:
        db_table = 'pypi_project'
        managed=False
