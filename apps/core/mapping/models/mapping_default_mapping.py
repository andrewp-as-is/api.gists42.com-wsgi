from django.conf import settings
#from django.contrib.postgres.search import SearchVectorField
from django.db import models

class DefaultMapping(models.Model):
    key = models.TextField(unique=True)
    value = models.TextField()

    is_approved = models.BooleanField(null=False,default=False)
    is_deleted = models.BooleanField(null=False,default=False)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True,related_name='+',on_delete=models.CASCADE)
    approved_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True,related_name='+',on_delete=models.CASCADE)
    deleted_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True,related_name='+',on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    approved_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)

    comments_count = models.IntegerField(null=True)

    class Meta:
        db_table = 'mapping_default_mapping'
        managed=False
