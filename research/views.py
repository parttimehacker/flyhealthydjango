from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from .forms import VolumeForm
from .models import Volume, Content, Section, Boilerplate
from rest_framework import viewsets
from .serializers import ContentSerializer, VolumeSerializer, BoilerplateSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@login_required
def dashboard_view(request):
    volume_list = Volume.objects.all()
    content_list = Content.objects.all()
    context = {'volume_list': volume_list, 'content_list': content_list, 'title': 'Dashboard'}
    return render(request, 'research/dashboard.html', context)


def insider_view(request):
    volume_list = Volume.objects.all().filter(published=True)
    volume_id = volume_list.first().number
    headline_list = Content.objects.filter(volume=volume_id)
    headline_list = headline_list.filter(section=Section.HEADLINES)
    around_list = Content.objects.filter(section=Section.AROUND, volume=volume_id)
    domestic_list = Content.objects.filter(section=Section.DOMESTIC, volume=volume_id)
    relevant_list = Content.objects.filter(section=Section.RELEVANT, volume=volume_id)
    context = {'volume_id': volume_id, 'volume_list': volume_list, 'headline_list': headline_list,
               'around_list': around_list, 'domestic_list': domestic_list, 'relevant_list': relevant_list,
               'title': 'INSIDER'}
    return render(request, 'research/insider.html', context)

@login_required
def draft_view(request):
    drafts = Volume.objects.all().filter(published=False)
    if drafts.count() == 1:
        volume_id = drafts.first().number
        print('draft id=',volume_id)
    else:
        volume_id = 0
    print('computed volume_id: ',volume_id)
    volume_list = Volume.objects.all()
    headline_list = Content.objects.filter(volume=volume_id)
    headline_list = headline_list.filter(section=Section.HEADLINES)
    around_list = Content.objects.filter(section=Section.AROUND, volume=volume_id)
    domestic_list = Content.objects.filter(section=Section.DOMESTIC, volume=volume_id)
    relevant_list = Content.objects.filter(section=Section.RELEVANT, volume=volume_id)
    context = {'volume_id': volume_id, 'volume_list': volume_list, 'headline_list': headline_list,
               'around_list': around_list, 'domestic_list': domestic_list, 'relevant_list': relevant_list,
               'title': 'Draft'}
    return render(request, 'research/draft.html', context)

def insider_by_volume_view(request, volume_id):
    volume_list = Volume.objects.all()
    headline_list = Content.objects.filter(section=Section.HEADLINES, pk=volume_id)
    around_list = Content.objects.filter(section=Section.AROUND, pk=volume_id)
    domestic_list = Content.objects.filter(section=Section.DOMESTIC, pk=volume_id)
    relevant_list = Content.objects.filter(section=Section.RELEVANT, pk=volume_id)
    context = {'volume': volume_id, 'volume_list': volume_list, 'headline_list': headline_list,
               'around_list': around_list, 'domestic_list': domestic_list, 'relevant_list': relevant_list,
               'title': 'INSIDER'}
    return render(request, 'research/insider.html', context)


@login_required
def research_view(request):
    volume_list = Volume.objects.all()
    content_list = Content.objects.all()
    context = {'volume_list': volume_list, 'content_list': content_list, 'title': 'Research'}
    return HttpResponseRedirect('/admin')
    # RedirectView.as_view(url='/admin')
    # return render(request, 'aci/admin/', context)


def volume_crud_view(request):
    context = {}
    # create object of form
    form = VolumeForm(request.POST or None, request.FILES or None)
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
    context['form'] = form
    return render(request, "research/volume_crud.html", context)

# views.py


class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all().order_by('volume')
    serializer_class = ContentSerializer

@csrf_exempt
def content_view(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        content = Content.objects.all()
        serializer = ContentSerializer(content, many=True)
        return JsonResponse(serializer.data, safe=False)

class VolumeViewSet(viewsets.ModelViewSet):
    queryset = Volume.objects.all().order_by('number')
    serializer_class = VolumeSerializer

@csrf_exempt
def volume_view(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        volumes = Volume.objects.all()
        serializer = VolumeSerializer(volumes, many=True)
        return JsonResponse(serializer.data, safe=False)

class BoilerplateViewSet(viewsets.ModelViewSet):
    queryset = Boilerplate.objects.all().order_by('volume')
    serializer_class = BoilerplateSerializer

@csrf_exempt
def boilerplate_view(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        boilerplate = Boilerplate.objects.all()
        serializer = BoilerplateSerializer(boilerplate, many=True)
        return JsonResponse(serializer.data, safe=False)