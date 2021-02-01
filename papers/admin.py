# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Paper
from . import models


@admin.register(models.Attachment, models.Support, models.Person)
class ItemAdmin(admin.ModelAdmin):
    pass


admin.site.register(Paper)
