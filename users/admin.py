from django.contrib import admin
from . import models


@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):

    """ Custom User Admin """

    list_display = (
        "avatar",
        "user_id",
        "user_name",
        "user_email",
        "user_position",
        "birthdate",
        "user_bio",
        "phone_num",
        "create_date",
        "update_date",
        "user_addr",
        "post_num",
        "is_cert",
    )
