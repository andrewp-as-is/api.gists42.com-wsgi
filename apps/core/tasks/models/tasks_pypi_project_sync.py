from django.db import models

from django_celery_task_queue.models import AbstractTask

class PypiProjectSync(AbstractTask):
    class Meta:
        db_table = 'tasks_pypi_project_sync'
        managed = False
