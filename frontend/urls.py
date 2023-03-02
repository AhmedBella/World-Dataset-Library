from django.urls import path
from .views import index, homepage
urlpatterns = [
    path('', index),
    path('homepage/', homepage), 
]
