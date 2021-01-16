from django.db import models
from django.utils.timezone import now
from core import models as core_models


class Attendance(core_models.TimeStampedModel):

    """ Attendance Model """

    date = models.DateField(auto_now_add=True)  # 날짜 기록

    time_start_work = models.DateTimeField(
        auto_now_add=True,
        null=True,
        verbose_name="출근시간",
    )  # 출근시간

    time_finish_work = models.DateTimeField(null=True, verbose_name="퇴근시간")  # 퇴근시간 기록

    user = models.ForeignKey(
        "users.User",
        related_name="attendances",
        on_delete=models.CASCADE,
    )
