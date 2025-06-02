# models.py

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    

    RELIGION_CHOICES = [
        ('hindu', 'Hindu'),
        ('muslim', 'Muslim'),
        ('christian', 'Christian'),
        ('other', 'Other'),
    ]

    LOCATION_CHOICES = [
        ('kerala', 'Kerala'),
        ('tamilnadu', 'Tamil Nadu'),
        ('karnataka', 'Karnataka'),
        ('other', 'Other'),
    ]

    PROFESSION_CHOICES = [
        ('engineer', 'Engineer'),
        ('doctor', 'Doctor'),
        ('teacher', 'Teacher'),
        ('business', 'Business'),
        ('other', 'Other'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    religion = models.CharField(max_length=100, choices=RELIGION_CHOICES)
    location = models.CharField(max_length=100, choices=LOCATION_CHOICES)
    profession = models.CharField(max_length=100, choices=PROFESSION_CHOICES)
    is_paid = models.BooleanField(default=False)
    mobile_no=models.CharField(max_length=10,validators=[  RegexValidator(
                regex=r'^\d{10}$',
                message='Mobile number must be exactly 10 digits.'
            )])
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)



class PartnerPreference(models.Model):
    RELIGION_CHOICES = UserProfile.RELIGION_CHOICES
    LOCATION_CHOICES = UserProfile.LOCATION_CHOICES
    PROFESSION_CHOICES = UserProfile.PROFESSION_CHOICES

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    min_age = models.PositiveIntegerField()
    max_age = models.PositiveIntegerField()
    preferred_religion = models.CharField(max_length=100, choices=RELIGION_CHOICES)
    preferred_location = models.CharField(max_length=100, choices=LOCATION_CHOICES)
    preferred_profession = models.CharField(max_length=100, choices=PROFESSION_CHOICES)



class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender.username} ➜ {self.receiver.username}: {self.content[:20]}'