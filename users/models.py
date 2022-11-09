from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  username = models.CharField(max_length = 50, blank = False, null = False, unique = True)
  email = models.EmailField( unique = True)
  password1 = models.CharField(max_length = 50, blank = True, null = False)
  password2 = models.CharField(max_length = 50, blank = True, null = False)
  bio = models.CharField(max_length = 50)
  
  class Meta:
    db_table = 'Users'
