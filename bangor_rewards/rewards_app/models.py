from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Charity(models.Model):
    name = models.CharField(max_length=64)
    points = models.IntegerField(default=0)
    mission_statement = models.CharField(max_length=360, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "charities"
