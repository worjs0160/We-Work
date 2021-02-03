from django.contrib import admin
from . import models



@admin.register(models.Position)
class Admin(admin.ModelAdmin):
    list_display = (
        "pk",
        "p_name",
    )


@admin.register(models.Department)
class Admin(admin.ModelAdmin):
    list_display = (
        "pk",
        "d_name",
    )

