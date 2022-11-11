from django import forms
from artists.models import *
from django.forms import ValidationError
from rest_framework import serializers
from authentication.serializers import *
class ArtistSerializer(serializers.ModelSerializer):
   # creation_datetime = serializers.DateTimeField(required = False)
    class Meta:
         model = Artist
         fields = '__all__'


class ArtistRegSerializer(serializers.ModelSerializer):
    user= LoginSerializer1()
    class Meta:
        model = Artist
        fields = '__all__'
   