from django.db import models
from artists.models import *

class Album(models.Model):
    name = models.CharField(max_length = 50,default = 'New Album')
    creation_datetime = models.DateTimeField(auto_now_add=True)
    release_datetime  = models.DateTimeField(blank = False)
    artist            = models.ForeignKey(Artist,related_name = 'albums',on_delete = models.CASCADE)
    cost              = models.FloatField()