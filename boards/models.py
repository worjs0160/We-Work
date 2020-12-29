from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from core import models as core_models

title_MinLenValidator = MinLengthValidator(2, "2자 이상 입력해주세요.(2자 ~ 80자 이내)")
title_MaxLenValidator = MaxLengthValidator(80, "80자 이내로 입력해주세요.(2자 ~ 80자 이내)")
contents_MinLenValidator = MinLengthValidator(2, "글이 너무 짧습니다. 2자 이상 입력해주세요.")


class Board(core_models.TimeStampedModel):
    class Meta:
        verbose_name = "공지사항"
        verbose_name_plural = "공지사항"

    postNo = models.AutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name="게시물 번호"
    )

    author = models.ForeignKey(
        "users.User",
        related_name="boards",
        on_delete=models.CASCADE,
        verbose_name="작성자",
    )
    title = models.CharField(
        max_length=80,
        validators=[title_MaxLenValidator, title_MinLenValidator],
        verbose_name="제목",
    )
    contents = models.TextField(
        blank=True, validators=[contents_MinLenValidator], verbose_name="내용"
    )

    viewCnts = models.PositiveIntegerField(default=0, verbose_name="조회수")
