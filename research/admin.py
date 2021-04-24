from django.contrib import admin

from .models import Volume, Content


class VolumeAdmin(admin.ModelAdmin):
    list_display = ('number', 'published',)


admin.site.register(Volume, VolumeAdmin)


class ContentAdmin(admin.ModelAdmin):
    list_display = ('volume', 'section', 'headline', 'posted', 'description', 'link')


admin.site.register(Content, ContentAdmin)
