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


@admin.register(models.Comment)
class CustomCommentAdmin(admin.ModelAdmin):
    """Custom Comment Admin"""

    list_display = (
        "author",
        "contents",
        "board",
    )