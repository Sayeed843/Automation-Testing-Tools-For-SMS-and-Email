from django.db import models
from django.contrib.auth.models import Permission, User
from django.conf import settings
import json
# Create your models here.
#
# class User(models.Model):
#     user_name = models.CharField(max_length=250)
#     campaign_name = models.CharField(max_length=350, blank=True)
#     api_key = models.CharField(max_length=350)
#
#     def __str__(self):
#         return user_name

class UserEmail(models.Model):
    user_name = models.CharField(max_length=250)
    campaign_name = models.CharField(max_length=350, blank=True)
    api_key = models.CharField(max_length=350)
    sender_email = models.CharField(max_length=350)
    receiver_email = models.CharField(max_length=350)
    email_subject = models.TextField(blank=False)
    email_body = models.TextField(blank=False)
    time = models.DateTimeField(auto_now_add=True)
    # count = models.AutoField(default=1)

    def __str__(self):
        return self.user_name+ "=>" +self.sender_email



class UserMessage(models.Model):
    user_name = models.CharField(max_length=250)
    campaign_name = models.CharField(max_length=350, blank=True)
    api_key = models.CharField(max_length=350)
    sender_number = models.CharField(max_length=350)
    receiver_number = models.CharField(max_length=350)
    mess_body= models.TextField(blank=False)
    time = models.DateTimeField(auto_now_add=True)
    # count = models.AutoField(default=1)

    def __str__(self):
        return self.user_name+ "=>" +self.sender_number
