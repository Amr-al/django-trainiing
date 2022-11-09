from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>', UserAPI.as_view()),
    path('',UsersAPI.as_view())
]
