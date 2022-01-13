from email import message
from unicodedata import name
from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=200,default="shubham")
    email=models.EmailField()
    message=models.TextField()
    def __str__(self):
        return f"{self.name} | {self.email}"