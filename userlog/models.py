from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Users(User):
    phone_number = models.CharField(max_length=11)
    birthdate = models.DateField()