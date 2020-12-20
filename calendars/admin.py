from django.contrib import admin
from . import models


@admin.register(models.CalendarType)
class TypeAdmin(admin.ModelAdmin):

    """ Type Admin Difinition """

    list_display = ("type_form", "used_by")

    def used_by(self, obj):
        return obj.calendars.count()


@admin.register(models.Calendar)
class CustomUserAdmin(admin.ModelAdmin):

    """ Custom Calendar Admin Difinition """

    list_display = (
        "host",
        "category",
        "start_time",
        "end_time",
        "title",
        "place",
        "schedule",
        "attached_file",
    )