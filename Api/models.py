from django.db import models

# Create your models here.
class Data(models.Model):
    file = models.FileField()