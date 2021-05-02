from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from .views import  dashboard_view, insider_view, research_view, content_view, volume_view, draft_view, boilerplate_view

urlpatterns = [
    path('aci/admin/', admin.site.urls, name='admin'),
    path('aci/dashboard/', dashboard_view, name='dashboard'),
    path('aci/insider/', insider_view, name='insider'),
    path('aci/draft/', draft_view, name='draft'),
    path('<int:volumne_id>/aci/insider/', insider_view, name='insider'),
    path('aci/research/', research_view, name='research'),
    path('aci/insider/api/volume/', volume_view, name='vapi'),
    path('aci/insider/api/article/', content_view, name='aapi'),
    path('aci/insider/api/boilerplate/', boilerplate_view, name='bapi'),
]

app_name = 'research'