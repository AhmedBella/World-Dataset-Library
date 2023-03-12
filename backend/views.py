from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from rest_framework import generics
from .serializers import DatasetSerializer
from .models import Dataset
from django.db.models import Q
# Create your views here.

class DatasetView(generics.CreateAPIView):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer

def dataset_list(request):
    query = request.GET.get('q') # Get the search query from the request parameters
    if query:
        datasets = Dataset.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    else:
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