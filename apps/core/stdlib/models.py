# from django.contrib.postgres.search import SearchVectorField
from django.db import models

class Stdlib(models.Model):
    name = models.TextField(unique=True)

    class Meta:
        db_table = 'stdlib_stdlib'
        managed=False
