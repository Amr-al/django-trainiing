from django import forms
from .models import *
from django.forms import ValidationError

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['name','release_datetime', 'artist' , 'cost' ,  'approved']