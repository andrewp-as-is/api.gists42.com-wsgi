from django.conf import settings
from django.db import models

class Token(models.Model):
    value = models.TextField(unique=True)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'token_token'
        managed=False
