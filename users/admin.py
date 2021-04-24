from django.contrib import admin

from .models import Researcher


class ResearcherAdmin(admin.ModelAdmin):
    list_display = ('name', 'organization', 'website')


admin.site.register(Researcher, ResearcherAdmin)
