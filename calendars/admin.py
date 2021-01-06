from django.contrib import admin
from . import models


@admin.register(models.Calendar)
class CustomUserAdmin(admin.ModelAdmin):

    """ Custom Calendar Admin Difinition """

    list_display = (
        "user",
        "start_time",
        "end_time",
        "title",
        "place",
        "schedule",
        "attached_file",
    )