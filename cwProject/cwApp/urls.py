from .import views
from django.urls import path

urlpatterns = [
    path('home/<link>/', views.index, name="index"),
    path('home/about/<link>/', views.about, name="about"),
    path('home/Base/<link>/', views.base, name="base"),
]