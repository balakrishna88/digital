
from urllib import request
from django.shortcuts import render

def Home(request):
    return render(request, 'website/index.html')