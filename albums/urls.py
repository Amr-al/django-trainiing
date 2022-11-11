from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', AlbumsView.as_view()),
    path('filter',AlbumsView2.as_view()),
    path('<int:pk>', AlbumView.as_view()),
    path('published/',AlbumsApprovedView.as_view()),
]
