from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from users.models import Researcher
from .forms import SignUpForm


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

    return render(request, 'app/signup.html', {'form': form})


@login_required
def dashboard_view(request):
    researcher_list = Researcher.objects.filter(admin=request.user)
    context = {'researcher_list': researcher_list}
    return render(request, 'templates/app/dashboard.html', context)


def landing_view(request):
    return render(request, 'templates/app/landing.html')
