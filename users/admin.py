from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    fieldsets = [
        (None, {"fields": ["username", "password", "user_name"]}),
        (
            "유저정보",
            {"fields": ["avatar", "user_department", "user_position", "user_bio"]},
        ),
        ("개인정보", {"fields": ["phone_num", "birthdate", "post_num", "user_addr"]}),
        ("인증정보", {"fields": ["is_cert", "is_superuser"]}),
    ]

    list_display = [
        "username",
        "password",
        "user_name",
        "user_department",
        "user_position",
        "phone_num",
        "birthdate",
        "user_addr",
        "post_num",
        "user_bio",
        "avatar",
        "is_cert",
        "is_superuser",
    ]
