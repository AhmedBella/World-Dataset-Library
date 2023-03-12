from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from rest_framework import generics
from .serializers import DatasetSerializer
from .models import Dataset
# Create your views here.

class DatasetView(generics.CreateAPIView):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer

def dataset_list(request):
    datasets = Dataset.objects.all()
    context = {'datasets': datasets}
    return render(request, 'dataset_list.html', context)

class DatasetDetailView(View):
    def get(self, request, id):
        dataset = get_object_or_404(Dataset, id=id)

        context = {
            'dataset': dataset,
        }

        return render(request, 'dataset_detail.html', context)