from django.db import models
from core import models as core_models


class Board(core_models.TimeStampedModel):
    postNo = models.CharField(max_length=8, blank=True, verbose_name="게시물 번호")

    author = models.ForeignKey(
        "users.User",
        related_name="boards",
        on_delete=models.CASCADE,
        verbose_name="작성자",
    )
    title = models.CharField(max_length=200, blank=True, verbose_name="제목")
    contents = models.TextField(blank=True, verbose_name="내용")

    viewCnts = models.PositiveIntegerField(default=0, verbose_name="조회수")

    class Meta:
        verbose_name = "공지사항"
        verbose_name_plural = "공지사항"
