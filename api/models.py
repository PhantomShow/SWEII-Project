from random import choices
from django.contrib import auth
from django.db import models

# Create your models here.

# User model for testing
class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return f"@{self.username}"

# Need to add both athlete and scout model

class Scout(auth.models.User):
    pass

class Athlete(auth.models.User, models.Model):
    height_foot_options = (
        (4, '4'),
        (5, '5'),
        (6, '6'), 
        (7, '7'),
    )
    height_inch_options = (
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'), 
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
        (11, '11'),
        (12, '12'),
    )
    age = models.IntegerField(default=18)
    weight_lb = models.IntegerField(default=140)
    height_ft = models.IntegerField(choices=height_foot_options, default=5)
    height_in = models.IntegerField(choices=height_inch_options, default=6)
    school = models.CharField(max_length=128, blank=True)