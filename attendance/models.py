from django.db import models
from django.utils.timezone import now
from core import models as core_models


class Attendance(core_models.TimeStampedModel):

    """ Attendance Model """

    date = models.DateField(auto_now=True)  # 날짜 기록
    time_go_work = models.DateTimeField(default=now, verbose_name="출근시간")  # 출근시간
    time_leave_work = models.DateTimeField(verbose_name="퇴근시간")  # 퇴근시간 기록

    user = models.ForeignKey(
        "users.User",
        related_name="attendances",
        on_delete=models.CASCADE,
        verbose_name="직원이름",
    )
