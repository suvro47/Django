from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=100, blank=False)
    institute = models.CharField(max_length=100, blank=False)
    country = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.username
