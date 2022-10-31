from django.urls import path
from applications import views

urlpatterns = [
    path('',views.index, name="applications-index"),
    path('cat/<slug>/',views.applicationsReadCat, name="applicationsblog-cat"),
    path('readBlog/<slug>/',views.applicationsReadBlog, name="applicationsreadblog"),
]