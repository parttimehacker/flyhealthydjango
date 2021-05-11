from django.contrib import admin

from .models import Volume, Content, Boilerplate


class VolumeAdmin(admin.ModelAdmin):
    list_display = ('number', 'published',)


admin.site.register(Volume, VolumeAdmin)


class ContentAdmin(admin.ModelAdmin):
    def get_changeform_initial_data(self, request):
        get_data = super(ContentAdmin, self).get_changeform_initial_data(request)
        get_data['created_by'] = request.user.pk
        return get_data
    list_display = ('volume', 'section', 'headline', 'posted', 'description', 'created_at')


admin.site.register(Content, ContentAdmin)


class BoilerplateAdmin(admin.ModelAdmin):
    list_display = ('volume', 'active', 'posted', 'section', 'headline', 'description')


admin.site.register(Boilerplate, BoilerplateAdmin)