from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Volume, Content, Frequency

@login_required
def dashboard_view(request):
    volume_list = Volume.objects.all()
    content_list = Content.objects.all()
    context = {'volume_list': volume_list, 'content_list': content_list,'title': 'Dashboard'}
    return render(request, 'research/dashboard.html', context)

def insider_view(request):
    static_list = Content.objects.filter(frequency=Frequency.STATIC)
    dynamic_list = Content.objects.filter(frequency=Frequency.DYNAMIC)
    context = {'static_list': static_list, 'dynamic_list': dynamic_list,'title': 'INSIDER'}
    return render(request, 'research/insider.html', context)

@login_required
def research_view(request):
    volume_list = Volume.objects.all()
    content_list = Content.objects.all()
    context = {'volume_list': volume_list, 'content_list': content_list,'title': 'Research'}
    return render(request, 'research/research.html', context)