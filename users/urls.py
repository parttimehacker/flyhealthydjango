from django.contrib import admin
from django.urls import path

from .views import signup_view, dashboard_view, landing_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup_view, name='sign-up'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('', landing_view, name='landing'),
]

app_name = 'users'
