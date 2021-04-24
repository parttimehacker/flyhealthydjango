from django.shortcuts import render

from .models import Volume, Content, Frequency


def dashboard_view(request):
    volume_list = Volume.objects.all()
    content_list = Content.objects.all()
    context = {'volume_list': volume_list, 'content_list': content_list,'title': 'Dashboard'}
    return render(request, 'research/dashboard.html', context)

def newsletter_view(request):
    static_list = Content.objects.filter(frequency=Frequency.STATIC)
    dynamic_list = Content.objects.filter(frequency=Frequency.DYNAMIC)
    context = {'static_list': static_list, 'dynamic_list': dynamic_list,'title': 'Newsletter'}
    return render(request, 'research/newsletter.html', context)
