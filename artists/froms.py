from django import forms
from .models import *
from django.forms import ValidationError

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'