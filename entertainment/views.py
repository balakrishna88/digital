from unicodedata import category
from django.shortcuts import render
import entertainment
from entertainment.models import posts_entertainment, Category_entertainment

# Create your views here.
def index(request):
    cat = Category_entertainment.objects.all()
    context = {'cat': cat}
    return render(request,'entertainment/index.html', context)

def entertainmentReadCat(request, slug):
    cats = Category_entertainment.objects.get(slug_nameentertainment = slug)
    blogs = posts_entertainment.objects.filter(category = cats)
    context = {'cat': cats, 'blogs': blogs}
    return render(request,'entertainment/read_cat.html', context)


def entertainmentReadBlog(request, slug):
    blog = posts_entertainment.objects.get(slug_postentertainment = slug)
    context = {'blog':blog}
    return render(request,'entertainment/read_blog.html', context)    