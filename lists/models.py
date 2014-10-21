from django.db import models

# Create your models here.

class List(models.Model):
   #list_= models.ListField()
   pass

class Item(models.Model):
   text = models.TextField(default='')
   list = models.ForeignKey(List, default='')

