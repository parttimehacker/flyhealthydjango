from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from users.models import Researcher
from .forms import SignUpForm

from rest_framework import viewsets
from .serializers import ResearcherSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('users:dashboard')
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('users:dashboard')
        else:
            messages.error(request, 'Correct the errors below')
    else:
        form = SignUpForm()

    return render(request, 'users/signup.html', {'form': form})


@login_required
def dashboard_view(request):
    researcher_list = Researcher.objects.filter(admin=request.user)
    context = {'researcher_list': researcher_list, 'title':'Dashboard'}
    return render(request, 'users/dashboard.html', context )

@login_required
def working_group_view(request):
    wg_list = Researcher.objects.all().order_by('name')
    cochairs_list = wg_list.filter(role='CO')
    airports_list = wg_list.filter(role='AI')
    associates_list = wg_list.filter(role='AS')
    context = {'cochairs_list': cochairs_list, 'airports_list': airports_list, 'associates_list':associates_list,
               'title': 'Working Group'}
    return render(request, 'users/workinggroup.html', context)


def landing_view(request):
    return render(request, 'users/landing.html')

class ResearcherViewSet(viewsets.ModelViewSet):
    queryset = Researcher.objects.all().order_by('name')
    serializer_class = ResearcherSerializer

@csrf_exempt
def researcher_view(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        content = Researcher.objects.all()
        serializer = ResearcherSerializer(content, many=True)
        return JsonResponse(serializer.data, safe=False)
