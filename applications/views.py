from unicodedata import category
from django.shortcuts import render
import applications
from applications.models import posts_application, Category_application

# Create your views here.
def index(request):
    cat = Category_application.objects.all()
    context = {'cat': cat}
    return render(request,'applications/index.html', context)

def applicationsReadCat(request, slug):
    cats = Category_application.objects.get(slug_nameapplications = slug)
    blogs = posts_application.objects.filter(category = cats)
    context = {'cat': cats, 'blogs': blogs}
    return render(request,'applications/read_cat.html', context)


def applicationsReadBlog(request, slug):
    blog = posts_application.objects.get(slug_postapplications = slug)
    context = {'blog':blog}
    return render(request,'applications/read_blog.html', context)    