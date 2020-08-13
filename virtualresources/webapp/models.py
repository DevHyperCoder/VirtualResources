from django.db import models
from django.contrib.auth.models import AbstractUser

# Extended User Model (UserProfile)
class UserProfile(AbstractUser):
    bio = models.CharField(max_length=1000)

# Product Model
class Product(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=500)
    price = models.PositiveIntegerField()
    seller = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        default=1)
    rating = models.PositiveIntegerField(default=0)


