from django.contrib import admin
from rest_framework.authtoken.models import Token
from users.models import CustomUser

admin.site.register(CustomUser)
