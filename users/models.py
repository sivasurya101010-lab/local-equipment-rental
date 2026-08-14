from django.db import models
from django.contrib.auth.models import AbstractUser

class TimestampedModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True,verbose_name="created at")
    updated_at=models.DateTimeField(auto_now=True,verbose_name="updated at")

    class meta:
        abstract=True 

class User(AbstractUser,TimestampedModel):

    class role(models.TextChoices):
        customer="CUSTOMER","Customer"
        owner="OWNER","Owner"

    role=models.CharField(max_length=20,choices=role.choices,default="CUSTOMER",verbose_name="user role")

    def __str__(self):
        return self.username


    