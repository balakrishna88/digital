from django.urls import path
from education import views

urlpatterns = [
    path('',views.index, name="education-index"),
    path('cat/<slug>/',views.educationReadCat, name="educationblog-cat"),
    path('readBlog/<slug>/',views.educationReadBlog, name="educationreadblog"),
]