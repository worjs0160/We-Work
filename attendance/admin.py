from django.contrib import admin
from . import models


@admin.register(models.Attendance)
class CustomAttendanceAdmin(admin.ModelAdmin):

    """ Custom Attendance Admin """

    list_display = (
        "user",
        "date",
        "time_start_work",
        "time_finish_work",
    )
