from django.contrib import auth
from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.

# User model
class CustomUser(auth.models.AbstractUser, auth.models.PermissionsMixin):
    user_type_choices = (
        (0, 'Scout'),
        (1, 'Athlete'),
    )
    school_options = (
        ('Georgia Institute of Technology', 'Georgia Institute of Technology'),
        ('Florida International University', 'Florida International University'),
        ('Yale', 'Yale'), 
        ('University of Pittsburgh', 'University of Pittsburgh'),
        ('Emory University','Emory University')
    )

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

    weight_lb = models.IntegerField(default=140, blank=True)
    height_ft = models.IntegerField(choices=height_foot_options, default=5, blank=True)
    height_in = models.IntegerField(choices=height_inch_options, default=6, blank=True)
    school = models.CharField(max_length=128, blank=True, choices=school_options)
    profile_pic = models.ImageField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True, default="No biography")
    gpa = models.FloatField(null=True, blank=True)

    user_type = models.PositiveSmallIntegerField(null=True, choices=user_type_choices)

    def get_absolute_url(self):
        return reverse("api:user_detail_page", kwargs={"pk": self.pk})

    def __str__(self):
        return f"@{self.username}"

class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('api:home_page')