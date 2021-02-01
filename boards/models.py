import os
from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from django.core.validators import MinLengthValidator, MaxLengthValidator
from core import models as core_models
from users.models import User

title_MinLenValidator = MinLengthValidator(2, "2자 이상 입력해주세요.(2자 ~ 80자 이내)")
title_MaxLenValidator = MaxLengthValidator(80, "80자 이내로 입력해주세요.(2자 ~ 80자 이내)")
contents_MinLenValidator = MinLengthValidator(10, "글이 너무 짧습니다. 10자 이상 입력해주세요.")


class Attachment(core_models.TimeStampedModel):

    board = models.ForeignKey(
        "Board", related_name="attachments", on_delete=models.CASCADE
    )

    file = models.FileField(upload_to="board-files/%Y-%m-%d/", blank=True, null=True)

    def filename(self):
        return os.path.basename(self.file.name)


class Comment(core_models.TimeStampedModel):
    # 댓글 모델

    class Meta:
        verbose_name = "댓글"
        verbose_name_plural = "댓글"

    author = models.ForeignKey(
        User,
        related_name="comments",
        on_delete=models.CASCADE,
        verbose_name="작성자",
    )

    board = models.ForeignKey(
        "Board", related_name="comments", on_delete=models.CASCADE, verbose_name="게시글"
    )
    contents = models.TextField(
        validators=[contents_MinLenValidator], verbose_name="내용"
    )


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
        validators=[contents_MinLenValidator], verbose_name="내용"
    )

    viewCnts = models.PositiveIntegerField(default=0, verbose_name="조회수")

    def __str__(self):
        return f"{self.title}({self.postNo})"

    def delete(self, *args, **kwargs):
        a = self.attachments.get(board=self)
        print(a.file)
        if a.file:
            os.remove(os.path.join(settings.MEDIA_ROOT, a.file.name))
        super().delete(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("boards:detail", kwargs={"pk": self.pk})

    @property
    def update_viewCnts(self):
        self.viewCnts += 1
        self.save()
        return self.viewCnts
