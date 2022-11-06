from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.core import serializers
from .models import *
import json
# Create your views 
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