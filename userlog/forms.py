from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Users

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Users   # Notice we now link to our model
        fields = ["username", "email", "phone_number", "birthdate", "password1", "password2"]