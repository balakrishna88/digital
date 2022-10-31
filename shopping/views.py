from unicodedata import category
from django.shortcuts import render
import shopping
from shopping.models import Blogsshopping, Categoryshopping

# Create your views here.
def index(request):
    cat = Categoryshopping.objects.all()
    context = {'cat': cat}
    return render(request,'shopping/index.html', context)

def shoppingReadCat(request, slug):
    cats = Categoryshopping.objects.get(slug_nameshopping = slug)
    blogs = Blogsshopping.objects.filter(category = cats)
    context = {'cat': cats, 'blogs': blogs}
    return render(request,'shopping/read_cat.html', context)


def shoppingReadBlog(request, slug):
    blog = Blogsshopping.objects.get(slug_postshopping = slug)
    context = {'blog':blog}
    return render(request,'shopping/read_blog.html', context)    