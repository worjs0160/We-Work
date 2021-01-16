from django.db import models
from core import models as core_models
from django.urls import reverse


class File(core_models.TimeStampedModel):

    """ File Model Definition """

    pass


class Calendar(core_models.TimeStampedModel):

    """ Calenadar Model Definition """

    user = models.ForeignKey(
        "users.User", related_name="calendars", on_delete=models.CASCADE
    )
    start_time = models.DateField(verbose_name="시작일")
    end_time = models.DateField(verbose_name="종료일")
    title = models.CharField(max_length=50, verbose_name="제 목")
    place = models.CharField(max_length=50, verbose_name="장 소")
    schedule = models.TextField(verbose_name="일정 내용")
    attached_file = models.FileField(blank=True, verbose_name="파일")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("calendars:event-detail", args=(self.id,))

    @property
    def get_html_url(self):
        url = reverse("calendars:event-detail", args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'