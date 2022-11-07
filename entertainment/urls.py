from django.urls import path
from entertainment import views

urlpatterns = [
    path('',views.index, name="entertainment-index"),
    path('cat/<slug>/',views.entertainmentReadCat, name="entertainmentblog-cat"),
    path('post/<slug>/',views.entertainmentReadBlog, name="entertainmentreadblog"),
]