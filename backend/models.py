from django.db import models
from django.contrib.auth.models import User

#defining the dataset model
##tags should be added, WIP
class Dataset(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    stars = models.IntegerField(default=0)
    public = models.BooleanField(default=False)
    #the datasets are linked to a user, if the user is deleted, the dataset is also deleted. this should be changed in the future, WIP
    user = models.ForeignKey(User, on_delete=models.CASCADE)
