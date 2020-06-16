# !/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models

"""
https://warehouse.pypa.io/api-reference/feeds/
https://pypi.org/rss/packages.xml
https://pypi.org/rss/updates.xml
"""


class _Item(models.Model):
    name = models.TextField()
    description = models.TextField(blank=True,null=True)
    pubdate = models.DateTimeField()

    class Meta:
        abstract = True

class NewProject(_Item):
    class Meta:
        db_table = 'pypi_rss_new_project'
        managed = False
        unique_together = [('name', 'pubdate',)]

class Update(_Item):
    version = models.TextField()

    class Meta:
        db_table = 'pypi_rss_latest_update'
        managed = False
        unique_together = [('name', 'pubdate',)]

