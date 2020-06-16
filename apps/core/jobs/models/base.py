from django.db import models

from .jobs_config import Config

class JobBase(models.Model):
    started_at = models.DateTimeField(blank=True,null=True)
    completed_at = models.DateTimeField(blank=True,null=True)
    locked_at = models.DateTimeField(blank=True,null=True)

    is_completed = models.BooleanField(default=False)
    is_locked = models.BooleanField(default=False,null=True)
    is_running = models.BooleanField(default=False,null=True)
    priority = models.SmallIntegerField(default=10)

    class Meta:
        abstract = True

    @property
    def task_name(self):
        return self._meta.db_table

    @classmethod
    def getonly(cls):
        return ('id','etag',) if hasattr(cls,'etag',) else ('id',)

    @classmethod
    def getkwargs(cls,ids):
        kwargs = {}
        for id in ids:
            kwargs[id] = {}
        return kwargs

    @classmethod
    def disable(cls):
        db_table = cls._meta.db_table
        Config.objects.filter(db_table=db_table).update(is_disabled=True)

    @classmethod
    def enable(cls):
        db_table = cls._meta.db_table
        Config.objects.filter(db_table=db_table).update(is_disabled=False)
