from rest_framework import serializers
from users.models import User
from artists.models import *
from rest_framework.exceptions import ValidationError
from django.contrib.auth.hashers import make_password , check_password
from django.contrib.auth import authenticate

def checkPassword(value):
    char = True
    digit = True
    for i in value:
        if i.lower() >= 'a' and i.lower() <= 'z':
            char = False
        if i.lower() >= '0' and i.lower() <= '9':
            digit = False
    print(char,digit, len(value))
    if char == True:
        raise ValidationError('password must contain at least one character')
    if digit == True:
        raise ValidationError('password must contain at least one digit')
    if len(value) < 6:
        raise ValidationError("password is too weak")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
    
class LoginSerializer1(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'email','bio')
        
class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid Details.")


class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(validators= [checkPassword])
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def create(self, validated_data):
        # print(make_password(validated_data['password1']) , check_password(validated_data['password2'],make_password(validated_data['password2'])))
        if validated_data['password1'] != validated_data['password2']:
            raise ValidationError("password1 is not match password2")
        try:
            user = User.objects.create_user(username = validated_data['username'], email = validated_data['email'].lower(),
         password = validated_data['password1'],
         password1 = make_password(validated_data['password1']),password2 =make_password(validated_data['password2']))
        except:
            ValidationError('Email must be unique')

        return user

