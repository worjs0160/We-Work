from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    list_display = (
        "avatar",
        "username",
        "password",
        "user_name",
        "user_position",
        "phone_num",
        "birthdate",
        "user_addr",
        "post_num",
        "user_bio",
        "is_cert",
    )
