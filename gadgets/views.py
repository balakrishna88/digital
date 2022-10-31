from unicodedata import category
from django.shortcuts import render
import gadgets
from gadgets.models import Blogsgadgets, Categorygadgets

# Create your views here.
def index(request):
    cat = Categorygadgets.objects.all()
    context = {'cat': cat}
    return render(request,'gadgets/index.html', context)

def gadgetsReadCat(request, slug):
    cats = Categorygadgets.objects.get(slug_namegadgets = slug)
    blogs = Blogsgadgets.objects.filter(category = cats)
    context = {'cat': cats, 'blogs': blogs}
    return render(request,'gadgets/read_cat.html', context)


def gadgetsReadBlog(request, slug):
    blog = Blogsgadgets.objects.get(slug_postgadgets = slug)
    context = {'blog':blog}
    return render(request,'gadgets/read_blog.html', context)    