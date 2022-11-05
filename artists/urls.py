from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', ArtistView.as_view()),
    path('<int:id>', ArtistView2.as_view()),
]
