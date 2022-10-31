from django.urls import path
from shopping import views

urlpatterns = [
    path('',views.index, name="shopping-index"),
    path('cat/<slug>/',views.shoppingReadCat, name="shoppingblog-cat"),
    path('readBlog/<slug>/',views.shoppingReadBlog, name="shoppingreadblog"),
]