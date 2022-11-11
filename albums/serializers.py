from artists.models import *
from django.forms import ValidationError
from rest_framework import serializers
from .models import *

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

class NewAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['name','release_datetime','cost','approved']