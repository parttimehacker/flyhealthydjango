from django.db import models


class Section(models.TextChoices):
    WELCOME = 'WE', 'Welcome'
    BACKGROUND = 'MF', 'Main Floor'
    HEADLINES = 'HE', 'Headlines & Major Buzz'
    DOMESTIC = 'DO', 'Domestic Headlines'
    AROUND = 'AR', 'From Around the Globe'
    PROGRESS = 'PR', 'Working Group Progress'
    RELEVANT = 'RE', 'Relevant Travel News'
    FEATURED = 'FE', 'Featured Resource'
    ABOUT = 'AB', 'About Us'
    GROUP = 'GR', 'Meet the Working Group'
    INDUSTRY = 'IN', 'Industry Groups & Helpful Links'
    CONTACT = 'CO', 'Contact Us'


class Volume(models.Model):
    number = models.IntegerField(primary_key=True)
    published = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-number', 'published', 'created_at']

    def __str__(self):
        return str(self.number)


class Frequency(models.TextChoices):
    STATIC = 'ST', 'Static'
    DYNAMIC = 'DY', 'Dynamic'


class Content(models.Model):
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE, default='')
    headline = models.CharField( max_length=256, default='')
    posted = models.DateField()
    description = models.TextField(default='')
    source = models.CharField( max_length=256, default='')
    link = models.URLField(default='')
    member = models.CharField( max_length=256, default='')

    section = models.CharField(
        max_length=2,
        choices=Section.choices,
        default=Section.DOMESTIC
    )

    frequency = models.CharField(
        max_length=2,
        choices=Frequency.choices,
        default=Frequency.STATIC
    )

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ['-volume', 'posted', 'headline']
