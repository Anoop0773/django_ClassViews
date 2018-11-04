from django.db import models
from django.contrib.auth.models import User


class Projects(models.Model):

    name = models.CharField(max_length=200)
    discription =  models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    
     
    def get_absolute_url(self):
        return "/project/%i/" % self.id

    def __str__(self):
        return self.name
