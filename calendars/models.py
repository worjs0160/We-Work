from django.db import models
from core import models as core_models


class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Item """

    type_form = models.CharField(max_length=10)

    class Meta:
        abstract = True

    def __str__(self):
        return self.type_form


class CalendarType(AbstractItem):

    """ Calendar Type Model Definition """

    class Meta:
        verbose_name = "Calendar Type"
        ordering = ["created"]


class File(core_models.TimeStampedModel):

    """ File Model Definition """

    pass


class Calendar(core_models.TimeStampedModel):

    """ Calenadar Model Definition """

    host = models.ForeignKey(
        "users.User", related_name="calendars", on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        "calendars.CalendarType", related_name="calendars", on_delete=models.CASCADE
    )
    start_time = models.DateField()
    end_time = models.DateField()
    title = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    schedule = models.CharField(max_length=200, blank=True)
    attached_file = models.FileField(blank=True)

    def __str__(self):
        return self.name