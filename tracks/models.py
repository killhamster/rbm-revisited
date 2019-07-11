from django.db import models

# Create your models here.
class Track(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField()
    version = models.CharField(max_length=40)
    image = models.FilePathField(path="/img")
    file = models.FilePathField(path="/music")
