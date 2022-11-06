from artists.models import *
from django.forms import ValidationError
from rest_framework import serializers
from .models import *

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'