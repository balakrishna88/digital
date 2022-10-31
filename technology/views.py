from unicodedata import category
from django.shortcuts import render
import technology
from technology.models import Blogstechnology, Categorytechnology

# Create your views here.
def index(request):
    cat = Categorytechnology.objects.all()
    context = {'cat': cat}
    return render(request,'technology/index.html', context)

def technologyReadCat(request, slug):
    cats = Categorytechnology.objects.get(slug_nametechnology = slug)
    blogs = Blogstechnology.objects.filter(category = cats)
    context = {'cat': cats, 'blogs': blogs}
    return render(request,'technology/read_cat.html', context)


def technologyReadBlog(request, slug):
    blog = Blogstechnology.objects.get(slug_posttechnology = slug)
    context = {'blog':blog}
    return render(request,'technology/read_blog.html', context)    