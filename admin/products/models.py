from django.db import models
from django.db.models import fields

class Product(models.Model):
    title = fields.CharField(max_length=200)
    image = fields.CharField(max_length=200)
    likes = fields.PositiveIntegerField(default=0)

class User(models.Model):
    pass
