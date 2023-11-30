from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    
class Novel(models.Model):
    title = models.CharField(max_length=200)
    published_date = models.DateTimeField("date published")
    year= models.IntegerField(default=0)
    status= models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null = True, blank= True)
    


    # votes = models.IntegerField(default=0)