from django.db import models

from django_celery_task_queue.models import AbstractTask

class PypiSimpleSync(AbstractTask):
    startswith = models.TextField(unique=True)

    class Meta:
        db_table = 'tasks_pypi_simple_sync'
        managed = False
