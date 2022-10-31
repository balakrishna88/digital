from django.urls import path
from automobiles import views

urlpatterns = [
    path('',views.index, name="automobiles-index"),
    path('cat/<slug>/',views.automobilesReadCat, name="automobilesblog-cat"),
    path('readBlog/<slug>/',views.automobilesReadBlog, name="automobilesreadblog"),
]