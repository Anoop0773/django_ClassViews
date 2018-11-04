from django.db import models
from django.contrib.auth.models import User
from projects.models import *


class Tasks(models.Model):
    name = models.CharField(max_length=200)
    discription =  models.TextField(blank=True, null=True)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    assigned_user = models.ForeignKey(User, on_delete=models.CASCADE,)

    def get_absolute_url(self):
        return "/task/%i/" % self.id
 
    def __str__(self):
        return self.name
