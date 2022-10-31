from django.urls import path
from dservices import views

urlpatterns = [
    path('',views.index, name="dservices-index"),
    path('cat/<slug>/',views.dservicesReadCat, name="dservicesblog-cat"),
    path('readBlog/<slug>/',views.dservicesReadBlog, name="dservicesreadblog"),
]