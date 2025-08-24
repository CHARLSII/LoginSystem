from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Users(AbstractUser):
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username