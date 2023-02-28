from django.db import models
from django.contrib.auth.models import User

#defining the dataset model
##tags should be added, WIP
class Dataset(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True, null=True)
    stars = models.IntegerField()
    #the datasets are linked to a user, if the user is deleted, the dataset is also deleted. this should be changed in the future, WIP
    user = models.ForeignKey(User, on_delete=models.CASCADE)
