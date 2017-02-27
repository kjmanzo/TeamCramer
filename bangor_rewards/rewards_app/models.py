from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Charitiy(models.Model):
    name = models.CharField(max_length=200)
    points = models.IntegerField(default=0)
    def __str__(self):
        return self.name

