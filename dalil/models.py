from django.db import models

# Create your models here.


class numbers(models.Model):
    phone_n = models.CharField(max_length=15)
    name = models.CharField(max_length=30)
