from enum import unique
from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


#foreign k=call

#category table
class Category_application(models.Model):
    cat_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=35)
    slug_nameapplications=AutoSlugField(populate_from='name', unique=True, null=True,default=None)

    def __str__(self):
        return self.name
   

class posts_application(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextUploadingField()
    pub_date = models.DateField(auto_now=True)
    category = models.ForeignKey(Category_application, on_delete=models.CASCADE)
    sub_category = models.CharField(max_length=100, blank=True)
    slug_postapplications=AutoSlugField(populate_from='title', unique=True, null=True,default=None)
  

    img = models.ImageField()
    

    def __str__(self):
        return self.title
   