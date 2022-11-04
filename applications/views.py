from unicodedata import category
from django.shortcuts import render
import applications
from applications.models import Blogsapplications, Categoryapplications

# Create your views here.
def index(request):
    cat = Categoryapplications.objects.all()
    context = {'cat': cat}
    return render(request,'applications/index.html', context)

def applicationsReadCat(request, slug):
    cats = Categoryapplications.objects.get(slug_nameapplications = slug)
    blogs = Blogsapplications.objects.filter(category = cats)
    context = {'cat': cats, 'blogs': blogs}
    return render(request,'applications/read_cat.html', context)


def applicationsReadBlog(request, slug):
    blog = Blogsapplications.objects.get(slug_postapplications = slug)
    context = {'blog':blog}
    return render(request,'applications/read_blog.html', context)    