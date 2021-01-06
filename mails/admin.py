from django.contrib import admin
from . import models


@admin.register(models.Mail)
class MailAdmin(admin.ModelAdmin):

    """ Custom User Admin """

    list_display = (
        "sender",
        "title",
        "mail_options",
        "appr_user",
        "created",
        "updated",
    )
