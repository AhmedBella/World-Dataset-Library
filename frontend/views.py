from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request, *args, **kwargs):
    return render(request, 'frontend/index.html')

def homepage(request):
    return HttpResponse('<h1>HomePage</h1>')
