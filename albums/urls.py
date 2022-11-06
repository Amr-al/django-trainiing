from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', AlbumView.as_view()),
    path('<int:pk>', AlbumView2.as_view()),
]
