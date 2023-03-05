from rest_framework import serializers
from .models import Dataset
class DatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dataset
        fields = ('id', 'name', 'description', 'created', 'updated', 'stars', 'public', 'user', 'file', 'license', 'creator', 'thumbnail',  )