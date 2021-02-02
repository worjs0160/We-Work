from django.contrib import admin
from . import models

class FileInline(admin.TabularInline):

    model = models.File


@admin.register(models.Calendar)
class CustomUserAdmin(admin.ModelAdmin):

    """ Custom Calendar Admin Difinition """

    inlines = (FileInline,)

    list_display = (
        "user",
        "start_time",
        "end_time",
        "title",
        "place",
        "schedule",
    )