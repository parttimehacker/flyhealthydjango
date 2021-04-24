from django.shortcuts import render

from .models import Content
from .models import PlatformType


def dashboard_view(request):
    static_list = Content.objects.filter(platform=PlatformType.RASPBERRYPI)
    dynamic_list = Project.objects.filter(platform=PlatformType.ESPRESSIF)
    arduino_list = Project.objects.filter(platform=PlatformType.ARDUINO)
    context = {'pi_list': pi_list, 'esp_list': esp_list, 'arduino_list': arduino_list, 'title': 'Internet of Things'}
    return render(request, 'iot/iot.html', context)
