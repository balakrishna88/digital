from django.urls import path
from technology import views

urlpatterns = [
    path('',views.index, name="technology-index"),
    path('cat/<slug>/',views.technologyReadCat, name="technologyblog-cat"),
    path('readBlog/<slug>/',views.technologyReadBlog, name="technologyreadblog"),
]