from unicodedata import category
from django.shortcuts import render
import automobiles
from automobiles.models import Blogsautomobiles, Categoryautomobiles

# Create your views here.
def index(request):
    cat = Categoryautomobiles.objects.all()
    context = {'cat': cat}
    return render(request,'automobiles/index.html', context)

def automobilesReadCat(request, slug):
    cats = Categoryautomobiles.objects.get(slug_nameautomobiles = slug)
    blogs = Blogsautomobiles.objects.filter(category = cats)
    context = {'cat': cats, 'blogs': blogs}
    return render(request,'automobiles/read_cat.html', context)


def automobilesReadBlog(request, slug):
    blog = Blogsautomobiles.objects.get(slug_postautomobiles = slug)
    context = {'blog':blog}
    return render(request,'automobiles/read_blog.html', context)    