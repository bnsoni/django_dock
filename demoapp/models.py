from django.db import models

# Create your models here.
class Interview(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    greeting = models.TextField()