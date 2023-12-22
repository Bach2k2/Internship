from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser

from django.urls import reverse


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    publish_date = models.DateField(auto_now_add=True)
    content = models.CharField(max_length=2000)

    def __unicode__(self):
        return self.content
    class Meta:
        db_table = 'Book'


class User(AbstractUser):
    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        # if self.is_superuser:
        #     self.is_customer = False
        #     self.is_admin = True
    # Delete not use field
    username = None
    is_staff = None
    is_superuser = None

    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'User'
