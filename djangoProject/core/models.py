from django.db import models

# Create your models here.

from django.db import models
class User(models.Model):
    username = models.CharField(max_length=80)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email_address = models.CharField(max_length=80)
    password = models.CharField(max_length=80)
    user_role = models.CharField(max_length=80)
    team_name = models.CharField(max_length=80)

class Planes(models.Model):
    plane_name = models.CharField(max_length=80)
    planes_count = models.IntegerField()

class Parts(models.Model):
    part_name = models.CharField(max_length=80)
    parts_count = models.IntegerField()

class Teams(models.Model):
    team_name = models.CharField(max_length=80)
    username = models.CharField(max_length=80)
    user_role = models.CharField(max_length=80)

