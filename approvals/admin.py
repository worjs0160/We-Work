from django.contrib import admin
from . import models



@admin.register(models.Draft)
class Admin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "created",
        "updated",
    )


@admin.register(models.Meeting)
class Admin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "created",
        "updated",
    )


@admin.register(models.Business)
class Admin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "created",
        "updated",
    )


@admin.register(models.Result)
class Admin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "created",
        "updated",
    )

@admin.register(models.Voucher)
class Admin(admin.ModelAdmin):
    
    list_display = (
        "title",
        "author",
        "created",
        "updated",
    )
