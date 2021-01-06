from django.contrib import admin
from . import models


@admin.register(models.Attendance)
class CustomAttendanceAdmin(admin.ModelAdmin):

    """ Custom Attendance Admin """

    list_display = (
        "user",
        "time_go_work",
        "time_leave_work",
    )
