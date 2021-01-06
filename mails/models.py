from django.db import models
from core import models as core_models


class Mail(core_models.TimeStampedModel):

    DEFAULT_EMAIL = "default"
    APPR_EMAIL = "appr"

    MAIL_CHOICES = (
        (DEFAULT_EMAIL, "Default"),
        (APPR_EMAIL, "Appr"),
    )

    sender = models.ForeignKey(
        "users.User",
        related_name="mails",
        on_delete=models.CASCADE,
        verbose_name="발신자",
    )

    recipient = models.CharField(max_length=50, verbose_name="수신자")
    reference = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="참조"
    )
    reference_hide = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="숨은 참조"
    )
    title = models.CharField(max_length=200, blank=True, verbose_name="제목")
    contents = models.TextField(blank=True, null=True, verbose_name="내용")

    mail_options = models.CharField(
        max_length=50, choices=MAIL_CHOICES, default=DEFAULT_EMAIL
    )
    appr_user = models.ForeignKey(
        "users.User",
        related_name="appr_mail",
        on_delete=models.CASCADE,
        verbose_name="승인자",
        blank=True,
        null=True,
    )
    # 파일 패스
    upload_files = models.FileField(
        upload_to="mail", null=True, blank=True, verbose_name="파일"
    )
    filename = models.CharField(
        max_length=64, blank=True, null=True, verbose_name="첨부파일명"
    )
