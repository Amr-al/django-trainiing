from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.core import serializers
from rest_framework.views import APIView
from .models import *
from .froms import *
from .serializers import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.permissions import IsAuthenticated,AllowAny, IsAdminUser
from rest_framework import generics, status
from authentication.serializers import *
from drf_multiple_model.views import ObjectMultipleModelAPIView
from rest_framework.response import Response
import json
# Create your views 
'''
class ArtistView(View):
    def post(self,request):
        try:
            form = ArtistForm(data = json.loads(request.body))
            if form.is_valid():
                form.save()
                return JsonResponse(form.data)
            return JsonResponse(form.errors, status=422)
        except:
            return JsonResponse({'message':'invalid format'},status = 500)

    def get(self,request):
        data = serializers.serialize('json',Artist.objects.all())
        return JsonResponse(json.loads(data) , safe= False)

class ArtistView2(View):
    
    def get(self,request,id):
        try:
            data = serializers.serialize('json',Artist.objects.filter(id = id))
        except Artist.DoesNotExist:
            return JsonResponse('Artist is not found', safe=False)

        return JsonResponse(json.loads(data) , safe= False)

    def delete(self,request , id):
        try:
            Artist.objects.filter(id = id)
            Artist.objects.filter(id = id).delete()
        except:
            return JsonResponse({'message':'ID not found'},safe= False)
        return JsonResponse({'message':'sucessfully deleted'} , safe = False)

    def put(self,request,id):
        try:
            form = ArtistForm(data = json.loads(request.body) ,instance = Artist.objects.get(id = id))
            if form.is_valid():
                form.save()
                return JsonResponse(form.data)
            return JsonResponse(form.errors, status=422)
        except:
            return JsonResponse({'message':'invalid format'},status = 500)
'''


class ArtistView(generics.ListCreateAPIView):
     queryset = Artist.objects.all()
     serializer_class = ArtistSerializer

class ArtistView2(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated | IsAdminUser]
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

#class ArtistRegister(ObjectMultipleModelAPIView,APIView):
#    querylist = [
#        {'queryset': User.objects.all(), 'serializer_class': UserSerializer},
#        {'queryset': Artist.objects.all(), 'serializer_class': ArtistSerializer}]

class ArtistRegister(APIView):
    def post(self,request):
        user=RegisterSerializer(data=request.data)
        if not user.is_valid():
            return Response(user.errors,status=status.HTTP_400_BAD_REQUEST)
        user.save()
        userobject=User.objects.get(username=request.data['username'])
        try:
            artistdata={
            'Stage_name':request.data['Stage_name'],
            'Social_link':request.data['Social_link'],
            'user':userobject.id
            }
        except:
            User.objects.get(username=request.data['username']).delete()
            return Response({'message':'missing stage_name or social_link'},status=status.HTTP_400_BAD_REQUEST)
        artist=ArtistSerializer(data=artistdata)
        if not artist.is_valid():
            User.objects.get(username=request.data['username']).delete()
            return Response(artist.errors,status=status.HTTP_400_BAD_REQUEST)
        artist.save()
        artist=Artist.objects.get(Stage_name=artist.data['Stage_name'])
        return Response(ArtistRegSerializer(Artist.objects.get(id=artist.id)).data)
        
        




