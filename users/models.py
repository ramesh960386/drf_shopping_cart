from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

gender_choices = [("M", "Male"), ("F", "Female"), ("O", "Others")]


class CustomUser(AbstractUser):
    gender = models.CharField(
        max_length=1, choices=gender_choices, default="M")

    def __str__(self):
        return self.username


# https://www.techiediaries.com/tutorial-django-rest-framework-building-products-manager-api/
# https://krakensystems.co/blog/2020/custom-users-using-django-rest-framework
# https://simpleisbetterthancomplex.com/tutorial/2018/11/22/how-to-implement-token-authentication-using-django-rest-framework.html
# https://tech.serhatteker.com/post/2020-09/enable-partial-update-drf/
