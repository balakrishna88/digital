from unicodedata import category
from django.shortcuts import render
import gservices
from gservices.models import Blogsgservices, Categorygservices

# Create your views here.
def index(request):
    cat = Categorygservices.objects.all()
    context = {'cat': cat}
    return render(request,'gservices/index.html', context)

def gservicesReadCat(request, slug):
    cats = Categorygservices.objects.get(slug_namegservices = slug)
    blogs = Blogsgservices.objects.filter(category = cats)
    context = {'cat': cats, 'blogs': blogs}
    return render(request,'gservices/read_cat.html', context)


def gservicesReadBlog(request, slug):
    blog = Blogsgservices.objects.get(slug_postgservices = slug)
    context = {'blog':blog}
    return render(request,'gservices/read_blog.html', context)    