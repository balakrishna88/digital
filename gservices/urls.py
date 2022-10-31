from django.urls import path
from gservices import views

urlpatterns = [
    path('',views.index, name="gservices-index"),
    path('cat/<slug>/',views.gservicesReadCat, name="gservicesblog-cat"),
    path('readBlog/<slug>/',views.gservicesReadBlog, name="gservicesreadblog"),
]