from django.contrib import admin

from .models import Archive


class ArchiveAdmin(admin.ModelAdmin):
    list_display = ('text',)


admin.site.register(Archive, ArchiveAdmin)
