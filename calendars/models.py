from django.db import models
from core import models as core_models
from django.urls import reverse
from django.contrib.auth.models import User


class File(core_models.TimeStampedModel):

    """ File Model Definition """

    pass


class Calendar(core_models.TimeStampedModel):

    """ Calenadar Model Definition """

    user = models.ForeignKey(
        "users.User", related_name="calendars", on_delete=models.CASCADE
    )
    start_time = models.DateField()
    end_time = models.DateField()
    title = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    schedule = models.TextField()
    attached_file = models.FileField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("calendars:event-detail", args=(self.id,))

    @property
    def get_html_url(self):
        url = reverse("calendars:event-detail", args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'