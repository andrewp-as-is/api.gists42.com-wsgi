from django.db import models

class Error(models.Model):
    db_table = models.TextField()
    job_id = models.IntegerField()
    type = models.TextField()
    value = models.TextField()
    traceback = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'jobs_error'
        managed = False
        ordering = ['-created_at']
