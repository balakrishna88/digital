from unicodedata import category
from django.shortcuts import render
import education
from education.models import Blogseducation, Categoryeducation

# Create your views here.
def index(request):
    cat = Categoryeducation.objects.all()
    context = {'cat': cat}
    return render(request,'education/index.html', context)

def educationReadCat(request, slug):
    cats = Categoryeducation.objects.get(slug_nameeducation = slug)
    blogs = Blogseducation.objects.filter(category = cats)
    context = {'cat': cats, 'blogs': blogs}
    return render(request,'education/read_cat.html', context)


def educationReadBlog(request, slug):
    blog = Blogseducation.objects.get(slug_posteducation = slug)
    context = {'blog':blog}
    return render(request,'education/read_blog.html', context)    