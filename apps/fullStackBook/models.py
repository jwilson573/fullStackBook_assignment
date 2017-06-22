from __future__ import unicode_literals

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    def __str__(self):
        return '%s %s %s' %(self.title, self.author, self.category)
