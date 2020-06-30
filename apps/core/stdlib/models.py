# from django.contrib.postgres.search import SearchVectorField
from django.db import models

class Stdlib(models.Model):
    slug = models.TextField()
    name = models.TextField(unique=True)

    class Meta:
        db_table = 'stdlib_stdlib'
        managed=False

    def save(self, *args, **kwargs):
        self.slug = self.name.lower()
        super().save(*args, **kwargs)
