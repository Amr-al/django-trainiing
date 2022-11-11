from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.core import serializers
from .models import *
from .serializers import *
from .filter import *
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny, IsAdminUser
import json
from django_filters import rest_framework as filters

# Create your views 
'''
class AlbumView(View):
    def post(self, request):
        try:
            Album = Album( name=json.loads(request.body)['name'], release_datetime=json.loads(request.body)[
                    'release_datetime'], artist=json.loads(request.body)['artist'], cost=json.loads(request.body)['cost'], approved=json.loads(request.body)['approved']).save()
        except:
            JsonResponse('Data is not valid' , safe= False)
        data = serializers.serialize('json', Album)
        return JsonResponse(json.loads(data), safe=False)

    def get(self,request):
        data = serializers.serialize('json',Album.objects.all())
        return JsonResponse(json.loads(data) , safe= False)

class AlbumView2(View):

    def get(self,request,id):
        try:
            data = serializers.serialize('json',Album.objects.filter(id = id))
        except Album.DoesNotExist:
            return JsonResponse('Album is not found', safe=False)
            
        return JsonResponse(json.loads(data) , safe= False)

    def put(self, request, id):
        Album.objects.filter(id=id).update( name=json.loads(request.body)['name'], release_datetime=json.loads(request.body)[
                    'release_datetime'], artist=json.loads(request.body)['artist'], cost=json.loads(request.body)['cost'], approved=json.loads(request.body)['approved'])
        data = serializers.serialize('json', Album.objects.filter(id=id))
        return JsonResponse(json.loads(data), safe=False)

    def delete(self, request, *args, **kwargs):
        try:
            Album.objects.filter(id=id).delete()
        except Album.DoesNotExist:
            return JsonResponse('Album is not exist', safe=False)
        data = serializers.serialize('json', Album.objects.all())
        return JsonResponse(json.loads(data), safe=False)
'''
'''
class AlbumView(generics.ListCreateAPIView):
     queryset = Album.objects.all()
     serializer_class = AlbumSerializer

class AlbumView2(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
'''
class AlbumsApprovedView(generics.ListAPIView):
    queryset = Album.objects.filter(approved=True)
    serializer_class = AlbumSerializer
    

def check(cost):
    if str("'") in cost or str('"') in cost :
        raise ValidationError("cost cant't be string")

class AlbumsView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class =  AlbumFilter
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated()]
        return []
    
    def post(self,request):
        try:
            artist=Artist.objects.get(id=self.request.user.artist.id)
        except Artist.DoesNotExist:
            return Response({'message':'Only artists can post albums'},status=status.HTTP_403_FORBIDDEN)
        album=NewAlbumSerializer(data=request.data)
        if not album.is_valid():
            return Response(album.errors,status=status.HTTP_400_BAD_REQUEST)
        
        try:
            albumobject={
            'name':'NewAlbum' if not 'name' in request.data else request.data['name'] ,
            'release_datetime':request.data['release_datetime'],
            'approved':request.data['approved'],
            'artist':artist.id,
            'cost':request.data['cost']
        }
        except:
            return Response({"message":"Enter all required data"},status=status.HTTP_400_BAD_REQUEST)
        album=AlbumSerializer(data=albumobject)
        if not album.is_valid():
            return Response(album.errors,status=status.HTTP_400_BAD_REQUEST)
        album.save()
        return Response(album.data)

class AlbumsView2(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated()]
        return []
    
    def post(self,request):
        try:
            artist=Artist.objects.get(id=self.request.user.artist.id)
        except Artist.DoesNotExist:
            return Response({'message':'Only artists can post albums'},status=status.HTTP_403_FORBIDDEN)
        album=NewAlbumSerializer(data=request.data)
        if not album.is_valid():
            return Response(album.errors,status=status.HTTP_400_BAD_REQUEST)
        
        try:
            albumobject={
            'name':'NewAlbum' if not 'name' in request.data else request.data['name'] ,
            'release_datetime':request.data['release_datetime'],
            'approved':request.data['approved'],
            'artist':artist.id,
            'cost':request.data['cost']
        }
        except:
            return Response({"message":"Enter all required data"},status=status.HTTP_400_BAD_REQUEST)
        album=AlbumSerializer(data=albumobject)
        if not album.is_valid():
            return Response(album.errors,status=status.HTTP_400_BAD_REQUEST)
        album.save()
        return Response(album.data)
    def get_queryset(self):
        queryset = Album.objects.all()

        if 'cost__gt' in self.request.query_params: 
                cost = self.request.query_params['cost__gt']
                check(cost)
                queryset = queryset.filter(cost__gt=cost)

        if 'cost__lt' in self.request.query_params: 
                cost = self.request.query_params['cost__lt']
                check(cost)
                queryset = queryset.filter(cost__lt=cost)
        
        if 'cost__gte' in self.request.query_params: 
                cost = self.request.query_params['cost__gte']
                check(cost)
                queryset = queryset.filter(cost__gte=cost)
        
        if 'cost__lte' in self.request.query_params: 
                cost = self.request.query_params['cost__lte']
                check(cost)
                queryset = queryset.filter(cost__lte=cost)
        
        if 'cost' in self.request.query_params: 
                cost = self.request.query_params['cost']
                check(cost)
                queryset = queryset.filter(cost=cost)
        
        if 'name' in self.request.query_params: 
                name = self.request.query_params['name']
                queryset = queryset.filter(name__icontains=name)
        
        return queryset

class AlbumView(APIView):
    def get(self,request,pk):
        try:
            album = AlbumSerializer(Album.objects.get(id=pk))
            return Response(album.data)
        except Album.DoesNotExist:
            return Response({"message": "Album does not exist"},status=status.HTTP_404_NOT_FOUND)
