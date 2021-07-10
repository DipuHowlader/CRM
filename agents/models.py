from django.db import models
from django.contrib.auth.models import User
from django.http import request

class Agent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.email