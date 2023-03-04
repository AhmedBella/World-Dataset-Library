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
    #this is the actual dataset file -->
    file = models.FileField(upload_to='uploads') #uploaded files will now be put in the uploads directory
    #the file must be limited to the accepted filetypes (like csv, json, etc..) WIP
    creator = models.CharField(max_length=200) #organisation or person who created the dataset originally
    license = models.CharField(max_length=200) #the license or terms of use for the data