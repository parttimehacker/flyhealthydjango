from django.contrib import admin
from django.urls import path

from .views import  dashboard_view, newsletter_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard_view, name='dashboard'),
    path('newsletter/', newsletter_view, name='newsletter'),
]

app_name = 'research'