from django.db import models

class Config(models.Model):
    db_table = models.TextField(unique=True)
    cls_name = models.TextField(unique=True)
    is_disabled = models.BooleanField(default=False)
    is_lockable = models.BooleanField(default=True)
    limit = models.IntegerField(default=0)

    class Meta:
        db_table = 'jobs_config'
        managed = False
