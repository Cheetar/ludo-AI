from django.db import models
from main.models import Code
# Create your models here.

class Contest(models.Model):
    title = models.CharField(max_length=200)
