from django.db import models


class Researcher(models.Model):
    name = models.CharField(max_length=128)
    organization = models.CharField(max_length=128, default='')
    website = models.URLField(default='')
