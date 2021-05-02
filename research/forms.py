# import form class from django
from django import forms

# import GeeksModel from models.py
from .models import Volume, Content


# create a ModelForm
class VolumeForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Volume
        fields = "__all__"

class ContentForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Content
        fields = "__all__"