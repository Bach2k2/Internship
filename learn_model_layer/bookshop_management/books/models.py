from __future__ import unicode_literals
from django.db import models

# from django.core.urlresolvers import reverse
from django.urls import reverse


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    publish_date = models.DateField(auto_now_add=True)
    content = models.CharField(max_length=2000)

    def __unicode__(self):
        return self.content
