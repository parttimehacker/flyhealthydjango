from django.contrib import admin
from django.urls import path, include

from .views import signup_view, dashboard_view, landing_view, home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup_view, name='sign-up'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('home/', home_view, name='home'),
    path( '', landing_view, name='landing' ),
]

app_name = 'users'