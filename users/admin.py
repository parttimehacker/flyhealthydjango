from django.contrib import admin

from .models import Researcher


class ResearcherAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'role', 'organization', 'public_allowed', 'email', 'website', 'created_at')


admin.site.register(Researcher, ResearcherAdmin)

