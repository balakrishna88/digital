from django.urls import path
from gadgets import views

urlpatterns = [
    path('',views.index, name="gadgets-index"),
    path('cat/<slug>/',views.gadgetsReadCat, name="gadgetsblog-cat"),
    path('readBlog/<slug>/',views.gadgetsReadBlog, name="gadgetsreadblog"),
]