from django.db import models
from artists.models import *


class Album(models.Model):
    name = models.CharField(max_length = 50,default = 'New Album')
    creation_datetime = models.DateTimeField(auto_now_add=True)
    release_datetime  = models.DateTimeField(blank = False)
    artist            = models.ForeignKey(Artist,related_name = 'albums',on_delete = models.CASCADE)
    cost              = models.FloatField()
    approved          = models.BooleanField(default = False)

    class Meta:
        db_table = 'Albums'
        constraints = [
           models.CheckConstraint( name='name must not contain any special characters or numbers',check = ~models.Q(name__regex = '[1-9]') or ~models.Q(name__regex = '[., +, *, ?, ^, $, (, ), [, ], {, }, |, \]'))
        ]
    def __str__(self):
        return self.name
    