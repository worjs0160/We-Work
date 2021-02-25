from django.contrib import admin
from . import models


@admin.register(models.Messenger)
class MessengerAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    pass
