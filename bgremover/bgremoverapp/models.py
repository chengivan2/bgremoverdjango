from django.db import models

# Create your models here.

class DownloadCounter(models.Model):
    time = models.DateTimeField()
    count = models.IntegerField()