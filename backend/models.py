from django.db import models
from django.contrib.auth.models import User
import os
from django.utils.text import slugify


# Define some necessary functions
def upload_to_dataset(instance, filename):
    # Generates the upload path for the dataset file
    return os.path.join('uploads', 'datasets', f'{slugify(instance.name)}{os.path.splitext(filename)[1]}')

def upload_to_thumbnail(instance, filename):
    # Generates the upload path for the dataset thumbnail
    return os.path.join('uploads', 'thumbnails', f'{slugify(instance.name)}{os.path.splitext(filename)[1]}')


# Define the Dataset model
## Add tags field in the future
class Dataset(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    stars = models.IntegerField(default=0)
    public = models.BooleanField(default=False)
    # Link the dataset to a user. If the user is deleted, the dataset is also deleted. This should be changed in the future.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Define the actual dataset file field
    file = models.FileField(upload_to=upload_to_dataset) # Uploaded files will now be put in the uploads directory.
    # Limit the file to accepted filetypes (e.g. csv, json). This is work in progress.

    creator = models.CharField(max_length=200) # Organization or person who created the dataset originally.
    license = models.CharField(max_length=200) # The license or terms of use for the data.
    thumbnail = models.ImageField(upload_to=upload_to_thumbnail)
    slug = models.SlugField(unique=True, max_length=100) # Define a slug field for the dataset with a maximum length of 100 characters

    def save(self, *args, **kwargs):
        # Overrides the save method to rename the uploaded file and thumbnail and set the slug field.
        if not self.slug:
            self.slug = slugify(self.name)
        if self.file:
            original_filename = os.path.basename(self.file.name)
            self.file.name = upload_to_dataset(self, original_filename)
        if self.thumbnail:
            original_filename = os.path.basename(self.thumbnail.name)
            self.thumbnail.name = upload_to_thumbnail(self, original_filename)
        super().save(*args, **kwargs)
