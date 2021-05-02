from django.contrib import admin
from django.urls import path

from .views import signup_view, dashboard_view, landing_view

urlpatterns = [
    path('aci/admin/', admin.site.urls, name='admin'),
    path('aci/signup/', signup_view, name='sign-up'),
    # path('dashboard/', dashboard_view, name='dashboard'),
    path('aci/', landing_view, name='landing'),
]

app_name = 'users'
