from django.db import models

# Create your models here.


class Lists(models.Model):
    title = models.CharField(max_length=100)


class Jobs(models.Model):
    title = models.CharField(max_length=100, default="x")
    job = models.CharField(max_length=1000)
    date = models.CharField(max_length=100, default="")
