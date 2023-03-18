import pandas as pd
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from rest_framework import generics
from .serializers import DatasetSerializer
from .models import Dataset
from django.db.models import Q
from django.urls import reverse_lazy
from .forms import DatasetForm
from django.views.generic.edit import CreateView

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

        if dataset.file.name.endswith('.csv'):
            df = pd.read_csv(dataset.file.path)
        elif dataset.file.name.endswith('.xlsx'):
            df = pd.read_excel(dataset.file.path)
        elif dataset.file.name.endswith('.json'):
            df = pd.read_json(dataset.file.path)
        else:
            return render(request, 'dataset_detail.html', {'error': 'Unsupported file format'})

        context = {
            'dataset': dataset,
            'headers': df.columns.values,
            'rows': df.values.tolist(),
        }

        return render(request, 'dataset_detail.html', context)
    
class DatasetCreateView(CreateView):
    model = Dataset
    form_class = DatasetForm
    template_name = 'dataset_create.html'
    success_url = reverse_lazy('dataset_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)