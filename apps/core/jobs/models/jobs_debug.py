from django.db import models

class Debug(models.Model):
    db_table = models.TextField()
    job_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    class Meta:
        db_table = 'jobs_debug'
        managed = False
