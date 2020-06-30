from django.contrib.postgres.search import SearchVectorField
from django.db import models

from pypi_slug import getslug

class Project(models.Model):
    slug = models.TextField(unique=True)
    name = models.TextField(unique=True)
    version = models.TextField(null=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'pypi_project'
        managed=False

    def save(self, *args, **kwargs):
        self.slug = getslug(self.name)
        super().save(*args, **kwargs)
