# !/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models

"""
https://warehouse.pypa.io/api-reference/xml-rpc/
"""

class Changelog(models.Model):
    name = models.TextField()
    version = models.TextField(null=True)
    timestamp = models.IntegerField()
    action = models.TextField()

    class Meta:
        db_table = 'pypi_xmlrpc_changelog'
        managed = False
        unique_together = [('timestamp','action',)]

