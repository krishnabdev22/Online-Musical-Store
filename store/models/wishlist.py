from django.db import models
from django.contrib.auth.models import User


class Wishlist(models.Model):
    product_id = models.CharField(max_length=200)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
