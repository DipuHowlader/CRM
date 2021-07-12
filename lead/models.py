from django.db import models
from django.contrib.auth.models import User
from agents.models import Agent


class Lead(models.Model):
    agent= models.ForeignKey(Agent, on_delete=models.CASCADE, blank=True, null= True)
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

