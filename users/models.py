from django.db import models


class Roles(models.TextChoices):
    COCHAIR = 'CO', 'Co-Chairs'
    AIRPORTS = 'AI', 'Airport Members'
    ASSOCIATES = 'AS', 'WBP/Associate Members'


class Researcher(models.Model):
    name = models.CharField(max_length=128)
    active = models.BooleanField(default=True)
    organization = models.CharField(max_length=128, default='')
    public_allowed = models.BooleanField(default=False)
    email = models.EmailField(default='')
    website = models.URLField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    role = models.CharField(
        max_length=2,
        choices=Roles.choices,
        default=Roles.AIRPORTS
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['role', 'name']

