import os
from django.conf import settings
from django.db import models
from core import models as core_models
from django.urls import reverse


class File(core_models.TimeStampedModel):

    """ File Model Definition """

    calendar = models.ForeignKey(
        "Calendar", related_name="attached_file", on_delete=models.CASCADE
    )

    file = models.FileField(upload_to="calendar-files/%Y-%m-%d/", blank=True, null=True, verbose_name="파일")

    def filename(self):
        return os.path.basename(self.file.name)


class Calendar(core_models.TimeStampedModel):

    """ Calenadar Model Definition """

    user = models.ForeignKey(
        "users.User", related_name="calendars", on_delete=models.CASCADE
    )
    start_time = models.DateTimeField(verbose_name="시작일")
    end_time = models.DateTimeField(verbose_name="종료일")
    title = models.CharField(max_length=50, verbose_name="제 목")
    place = models.CharField(max_length=50, verbose_name="장 소")
    schedule = models.TextField(verbose_name="일정 내용")
    all_day = models.BooleanField(default=False, verbose_name="하루 종일")

    def __str__(self):
        return self.title

    @property
    def get_month_html_url(self):
        url = reverse("calendars:event-month-detail", args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'

    @property
    def get_week_html_url(self):
        url = reverse("calendars:event-week-detail", args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'

    @property
    def get_day_html_url(self):
        url = reverse("calendars:event-day-detail", args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'

    def get_id(self):
        return self.user

    def delete(self, *args, **kwargs):
        a = self.attached_file.get(calendar=self)
        if a.file:
            os.remove(os.path.join(settings.MEDIA_ROOT, a.file.name))
        super().delete()

    

