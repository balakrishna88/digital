from unicodedata import category
from django.shortcuts import render
import travel
from travel.models import Blogstravel, Categorytravel

# Create your views here.
def index(request):
    cat = Categorytravel.objects.all()
    context = {'cat': cat}
    return render(request,'travel/index.html', context)

def travelReadCat(request, slug):
    cats = Categorytravel.objects.get(slug_nametravel = slug)
    blogs = Blogstravel.objects.filter(category = cats)
    context = {'cat': cats, 'blogs': blogs}
    return render(request,'travel/read_cat.html', context)


def travelReadBlog(request, slug):
    blog = Blogstravel.objects.get(slug_posttravel = slug)
    context = {'blog':blog}
    return render(request,'travel/read_blog.html', context)    