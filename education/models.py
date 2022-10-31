from enum import unique
from django.db import models
from autoslug import AutoSlugField

#foreign k=call

#category table
class Categoryeducation(models.Model):
    cat_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=35)
    slug_nameeducation=AutoSlugField(populate_from='name', unique=True, null=True,default=None)

    def __str__(self):
        return self.name
   

class Blogseducation(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateField(auto_now=True)
    category = models.ForeignKey(Categoryeducation, on_delete=models.CASCADE)
    sub_category = models.CharField(max_length=100, blank=True)
    slug_posteducation=AutoSlugField(populate_from='title', unique=True, null=True,default=None)
  

    img = models.ImageField()
    

    def __str__(self):
        return self.title
   