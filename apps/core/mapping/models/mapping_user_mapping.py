from django.conf import settings
# from django.contrib.postgres.search import SearchVectorField
from django.db import models

class UserMapping(models.Model):
    slug = models.TextField()
    name = models.TextField(unique=True)
    value = models.TextField()

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'mapping_user_mapping'
        managed=False
        unique_together = [('created_by','name',),]

    def save(self, *args, **kwargs):
        self.slug = self.name.lower()
        super().save(*args, **kwargs)
