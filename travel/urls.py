from django.urls import path
from travel import views

urlpatterns = [
    path('',views.index, name="travel-index"),
    path('cat/<slug>/',views.travelReadCat, name="travelblog-cat"),
    path('readBlog/<slug>/',views.travelReadBlog, name="travelreadblog"),
]