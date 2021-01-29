from django.contrib import admin
from . import models


class AttachmentInline(admin.TabularInline):

    model = models.Attachment


@admin.register(models.Board)
class CustomBoardAdmin(admin.ModelAdmin):

    """ Custom User Admin """

    inlines = (AttachmentInline,)

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