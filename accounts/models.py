from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH
from django.contrib.auth.models import AbstractUser
# from django.db.models.signals import post_save

# Custom user class
class User(AbstractUser):
    is_agent = models.BooleanField(default=False)
