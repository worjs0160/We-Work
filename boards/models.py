from django.db import models
from core import models as core_models


class Board(core_models.TimeStampedModel):
    author = models.ForeignKey(
        "users.User",
        related_name="boards",
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=200, blank=True)
    board_num = models.CharField(max_length=8, blank=True)

    view_cnts = models.PositiveIntegerField()
    contents = models.TextField(blank=True)
