from django.db import models
from django.contrib.auth.models import User
import os
from django.utils.text import slugify


#some necessary functions-->
def upload_to_dataset(instance, filename):
    #Generates the upload path for the dataset file
    return os.path.join('uploads', 'datasets', f'{slugify(instance.name)}{os.path.splitext(filename)[1]}')

def upload_to_thumbnail(instance, filename):
    #Generates the upload path for the dataset thumbnail
    return os.path.join('uploads', 'thumbnails', f'{slugify(instance.name)}{os.path.splitext(filename)[1]}')


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
    file = models.FileField(upload_to=upload_to_dataset) #uploaded files will now be put in the uploads directory
    #the file must be limited to the accepted filetypes (like csv, json, etc..) WIP

    creator = models.CharField(max_length=200) #organisation or person who created the dataset originally
    license = models.CharField(max_length=200) #the license or terms of use for the data
    thumbnail = models.ImageField(upload_to=upload_to_thumbnail)

    def save(self, *args, **kwargs):
        #Overrides the save method to rename the uploaded file and thumbnail#
        if self.file:
            original_filename = os.path.basename(self.file.name)
            self.file.name = upload_to_dataset(self, original_filename)
        if self.thumbnail:
            original_filename = os.path.basename(self.thumbnail.name)
            self.thumbnail.name = upload_to_thumbnail(self, original_filename)
        super().save(*args, **kwargs)
