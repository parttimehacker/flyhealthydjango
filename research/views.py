from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Volume, Content, Frequency, Section

@login_required
def dashboard_view(request):
    volume_list = Volume.objects.all()
    content_list = Content.objects.all()
    context = {'volume_list': volume_list, 'content_list': content_list,'title': 'Dashboard'}
    return render(request, 'research/dashboard.html', context)

def insider_view(request):
    headline_list = Content.objects.filter(section=Section.HEADLINES)
    around_list = Content.objects.filter(section=Section.AROUND)
    domestic_list = Content.objects.filter(section=Section.DOMESTIC)
    relevant_list = Content.objects.filter(section=Section.RELEVANT)
    context = {'headline_list': headline_list, 'around_list': around_list, 'domestic_list':domestic_list,
               'relevant_list':relevant_list, 'title': 'INSIDER'}
    return render(request, 'research/insider.html', context)

@login_required
def research_view(request):
    volume_list = Volume.objects.all()
    content_list = Content.objects.all()
    context = {'volume_list': volume_list, 'content_list': content_list,'title': 'Research'}
    return render(request, 'research/research.html', context)