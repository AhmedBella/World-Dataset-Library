from django.shortcuts import render
from rest_framework import generics
from .serializers import DatasetSerializer
from .models import Dataset
# Create your views here.

class DatasetView(generics.CreateAPIView):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer
    