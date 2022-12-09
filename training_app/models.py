from django.db import models

# Create your models here.

#Roles choices
ROLE_CHOICES = (
        ('User', 'User'),
        ('TL', 'TL'),
        ('Admin', 'Admin')
    )

class User(models.Model):
    user_id = models.IntegerField()
    email = models.EmailField(unique=True)
    user_role = models.CharField(max_length=32, choices=ROLE_CHOICES)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField()

class Training(models.Model):
    training_id = models.IntegerField()
    training_course = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now = True)
    updated = models.DateTimeField(auto_now_add = True)
    description = models.TextField()
    
class Review(models.Model):
    review_id = models.IntegerField()
    reviewer_name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now = True)
    updated = models.DateTimeField(auto_now_add = True)

class Assignment(models.Model):
    assignment_id = models.IntegerField()
    assignment_course = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now = True)
    updated = models.DateTimeField(auto_now_add = True)
    description = models.TextField()
    
class Client(models.Model):
    client_id = models.IntegerField()
    client_name = models.CharField(max_length=40) 


