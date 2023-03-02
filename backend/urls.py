from django.urls import path
from .views import DatasetView

urlpatterns = [
    path('dataset/', DatasetView.as_view()), 
]
