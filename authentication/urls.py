from django.contrib import admin
from django.urls import path
from .views import *
from knox import views as knox_views
from .views import *
urlpatterns = [
    path('register/', Register.as_view()),
    path(r'login/', LoginAPI.as_view(), name='knox_login'),
    path(r'logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path(r'logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
]
