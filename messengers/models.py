from django.db import models
from core import models as core_models


class Messenger(core_models.TimeStampedModel):

    """ Messenger Model Definition """

    participants = models.ManyToManyField(
        "users.User", related_name="messenger", blank=True
    )


class Message(core_models.TimeStampedModel):

    """ Message Model Definition """

    sender = models.ForeignKey(
        "users.User", related_name="messages", on_delete=models.CASCADE
    )
    receiver = models.ForeignKey(
        "Messenger", related_name="messages", on_delete=models.CASCADE
    )

    message = models.TextField(null=True)

    def __str__(self):
        return f"{self.sender} says : {self.message}"