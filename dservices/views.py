from unicodedata import category
from django.shortcuts import render
import dservices
from dservices.models import Blogsdservices, Categorydservices

# Create your views here.
def index(request):
    cat = Categorydservices.objects.all()
    context = {'cat': cat}
    return render(request,'dservices/index.html', context)

def dservicesReadCat(request, slug):
    cats = Categorydservices.objects.get(slug_namedservices = slug)
    blogs = Blogsdservices.objects.filter(category = cats)
    context = {'cat': cats, 'blogs': blogs}
    return render(request,'dservices/read_cat.html', context)


def dservicesReadBlog(request, slug):
    blog = Blogsdservices.objects.get(slug_postdservices = slug)
    context = {'blog':blog}
    return render(request,'dservices/read_blog.html', context)    