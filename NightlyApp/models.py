from django.db import models

# Create your models here.


class Day(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    closing_manager = models.CharField(max_length=200)
    headwait = models.CharField(max_length=200)
