from django.contrib import admin
from django.urls import path

from .views import signup_view, dashboard_view, landing_view, researcher_view, working_group_view

urlpatterns = [
    path('aci/admin/', admin.site.urls, name='admin'),
    path('aci/signup/', signup_view, name='sign-up'),
    path('aci/', landing_view, name='landing'),
    path( 'aci/workinggroup', working_group_view, name='workinggroup' ),
    path('aci/insider/api/researchers/', researcher_view, name='rapi'),
]

app_name = 'users'
