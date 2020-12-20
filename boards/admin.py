from django.contrib import admin
from . import models


@admin.register(models.Board)
class CustomBoardAdmin(admin.ModelAdmin):

    """ Custom User Admin """

    list_display = (
        "postNo",
        "author",
        "title",
        "contents",
        "viewCnts",
        "created",
        "updated",
    )
