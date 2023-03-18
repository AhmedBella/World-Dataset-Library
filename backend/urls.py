from django.urls import path
from .views import *

urlpatterns = [
    path('dataset/', DatasetView.as_view(), name='create_dataset'), 
    path('list/', dataset_list, name='dataset_list'),
    path('<int:id>/', DatasetDetailView.as_view(), name='dataset_detail'),
    path('create/', DatasetCreateView.as_view(), name='create-dataset'),

]
