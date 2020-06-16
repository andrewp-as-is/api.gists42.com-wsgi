from django.db import models

class Queue(models.Model):
    db_table = models.TextField()
    job_id = models.IntegerField()
    pushed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'jobs_queue'
        managed = False
