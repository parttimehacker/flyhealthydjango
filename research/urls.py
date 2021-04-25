from django.contrib import admin
from django.urls import path

from .views import  dashboard_view, insider_view, research_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('insider/', insider_view, name='insider'),
    path('research/', research_view, name='research'),
]

app_name = 'research'