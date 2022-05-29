from argparse import ONE_OR_MORE
from turtle import onclick
from unicodedata import name
from django.db import models

# Create your models here.


class category(models.Model):
    name= models.CharField(max_length=100,null=False, blank=False)

    def __str__(self):
        return self.name

class photo(models.Model):
   category= models.ForeignKey(category, on_delete=models.SET_NULL)
   image= models.ImageField(null=False, blank=False)

  
