from django import forms
from artists.models import *
from django.forms import ValidationError
from rest_framework import serializers

class ArtistSerializer(serializers.ModelSerializer):
   # creation_datetime = serializers.DateTimeField(required = False)
    class Meta:
         model = Artist
         fields = '__all__'



   