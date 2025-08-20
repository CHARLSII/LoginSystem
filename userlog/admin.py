from django.contrib import admin
from .models import Users

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'first_name', 'last_name', 'phone_number', 'birthdate')
    
    search_fields = ('username', 'birthdate')


admin.site.register(Users, UserAdmin)