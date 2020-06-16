from django.db import models

class Log(models.Model):
    db_table = models.TextField()
    job_id = models.IntegerField()

    pushed_at = models.DateTimeField()
    started_at = models.DateTimeField()
    completed_at = models.DateTimeField()

    is_completed = models.BooleanField(null=True)
    is_restarted = models.BooleanField(null=True)
    is_locked = models.BooleanField(null=True)
    is_deleted = models.BooleanField(null=True)

    class Meta:
        db_table = 'jobs_log'
        managed = False
