from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from users.models import *
from rest_framework import status
from rest_framework.views import APIView
from .serializers import *
from django.contrib.auth.hashers import make_password , check_password
from knox.views import LoginView as KnoxLoginView
from rest_framework.authentication import BasicAuthentication
from django.contrib.auth import login

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        try:
            data = UserSerializer( User.objects.get(username= request.data['username']) )
            alldata = LoginSerializer1(User.objects.get(username= request.data['username']))
            print(check_password(request.data['password'], make_password(request.data['password'])))
            if check_password(request.data['password'], make_password(request.data['password'])) == False:
                raise Exception('User is not exist')
        except User.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
        return Response({
            "token": AuthToken.objects.create(user)[1],
            "user": alldata.data

        })


class Register(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "username": serializer.data['username'],
                "email": serializer.data['email'],
                "password": serializer.data['password1']})
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)



        
        




