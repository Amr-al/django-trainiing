from django.shortcuts import render
from .models import User
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from authentication.serializers import LoginSerializer1
from rest_framework.response import Response
from rest_framework import status


class UserAPI(APIView):
    permission_classes = [IsAuthenticated ]

    def get(self, request, pk):
        try:
            user = LoginSerializer1(User.objects.get(id=pk))
            return Response(user.data)
        except User.DoesNotExist:
            return Response({"message": "User does not exist"},status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            user = LoginSerializer1(
                data=request.data, instance=User.objects.get(id=pk))
            if self.request.user.id != pk:
                return Response({'message': 'Not authorized'},status= status.HTTP_403_FORBIDDEN)
            print(self.request.user)
            if user.is_valid():
                user.save()
                return Response(user.data)
            return Response(user.errors)
        except User.DoesNotExist:
            return Response({"message": "User does not exist"}, status= status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk):
        try:
            user = LoginSerializer1(
                data=request.data, instance=User.objects.get(id=pk), partial = True)
           
            if self.request.user.id != pk:
                return Response({'message': 'Not authorized'},status= status.HTTP_403_FORBIDDEN)
          
            if user.is_valid():
                user.save()
                return Response(user.data)
            return Response(user.errors)
        except User.DoesNotExist:
            return Response({"message": "User does not exist"}, status= status.HTTP_404_NOT_FOUND)


class UsersAPI(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request):
        user = LoginSerializer1(User.objects.all(),many=True)  
        return Response(user.data)