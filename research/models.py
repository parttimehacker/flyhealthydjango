from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Section(models.TextChoices):
    HEADLINES = 'HE', 'Headlines & Major Buzz'
    DOMESTIC = 'DO', 'Domestic Headlines'
    AROUND = 'AR', 'From Around the Globe'
    RELEVANT = 'RE', 'Relevant Travel News'
    FEATURED = 'FE', 'Featured Resource'
    INDUSTRY = 'IN', 'Industry Groups & Helpful Links'


class StaticText(models.TextChoices):
    WELCOME = 'WE', 'Welcome'
    BACKGROUND = 'MF', 'Background'
    DISCLAIMER = 'DI', 'Disclaimer'
    ABOUT = 'AB', 'About Us'
    GROUP = 'GR', 'Meet the Working Group'
    CONTACT = 'CO', 'Contact Us'


class Volume(models.Model):
    number = models.IntegerField(primary_key=True)
    published = models.BooleanField(default=False)
    published_at = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-number', 'published_at', 'created_at']

    def __str__(self):
        return str(self.number)


class Content(models.Model):
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE, default='', related_name='articles')
    headline = models.CharField(max_length=256, default='')
    posted = models.DateField()
    description = models.TextField(default='')
    source = models.CharField(max_length=256, default='')
    link = models.URLField(default='')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, )

    section = models.CharField(
        max_length=2,
        choices=Section.choices,
        default=Section.HEADLINES
    )

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ['-volume', 'section', 'headline']
        unique_together = ('volume', 'section', 'headline')


class Boilerplate(models.Model):
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE, default='', related_name='boilerplate')
    active = models.BooleanField(default=True)
    posted = models.DateField()
    headline = models.CharField(max_length=256, default='')
    description = models.TextField(default='')

    section = models.CharField(
        max_length=2,
        choices=StaticText.choices,
        default=StaticText.WELCOME
    )