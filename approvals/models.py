from django.db import models
from core.models import (
    TimeStampedModel,
    title_MaxLenValidator,
    title_MinLenValidator,
    contents_MinLenValidator,
)

# Create your models here.


class DocBase(TimeStampedModel):
    """
    결재서류 Base 클래스(공통내용)
    """

    STA_REQ = "reqest"
    STA_REV = "review"
    STA_APP = "approved"
    STA_RET = "return"

    STA_CHOICES = (
        (STA_REQ, "결재전"),
        (STA_REV, "결재중"),
        (STA_APP, "결재완료"),
        (STA_RET, "결재반려"),
    )

    author = models.ForeignKey(
        "users.User", related_name="%(class)s".lower(), on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=80,
        validators=[title_MaxLenValidator, title_MinLenValidator],
        verbose_name="제목",
    )
    contents = models.TextField(
        validators=[contents_MinLenValidator], verbose_name="내용"
    )

    viewer = models.ManyToManyField(
        "users.User",
        related_name="%(class)s".lower() + "_viewer",
        blank=True,
        verbose_name="열람자",
    )

    status = models.CharField(
        choices=STA_CHOICES, max_length=10, default=STA_REQ, verbose_name="결재상황"
    )

    class Meta:
        abstract = True


class Draft(DocBase):
    """
    기안서 클래스
    """

    class Meta:
        verbose_name = "기안서"
        verbose_name_plural = "기안서"

    pass


class Meeting(DocBase):
    """
    회의보고서
    """

    class Meta:
        verbose_name = "회의보고서"
        verbose_name_plural = "회의보고서"

    pass


class Business(DocBase):
    """
    업무보고서
    """

    class Meta:
        verbose_name = "업무보고서"
        verbose_name_plural = "업무보고서"

    pass


class Result(DocBase):
    """
    결과보고서
    """

    class Meta:
        verbose_name = "결과보고서"
        verbose_name_plural = "결과보고서"

    pass


class Voucher(DocBase):
    """
    지출결의서
    """

    class Meta:
        verbose_name = "지출결의서"
        verbose_name_plural = "지출결의서"

    pass
