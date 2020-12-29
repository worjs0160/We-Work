from django.contrib import admin
from . import models


@admin.register(models.Board)
class CustomBoardAdmin(admin.ModelAdmin):

    """ Custom User Admin """

    list_display = (
        "title",
        "author",
        "viewCnts",
        "postNo",
        "created",
        "updated",
    )
