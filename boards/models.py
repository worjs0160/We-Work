import os
from uuid import uuid4
from datetime import datetime
from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from core import models as core_models
from core.managers import CustomManager
from users.models import User



def get_file_path(instance, filename):
    """
    uuid4를 활용한 암호화된 파일 경로를 설정
    """
    ymd_path = datetime.now().strftime('%Y/%m/%d')
    uuid_name = uuid4().hex
    return '/'.join(['board-files/', ymd_path, uuid_name])


class Attachment(core_models.TimeStampedModel):

    board = models.ForeignKey(
        "Board", related_name="attachments", on_delete=models.CASCADE
    )

    file = models.FileField(upload_to=get_file_path, blank=True, null=True)
    filename = models.CharField(max_length=80, null=True, verbose_name="첨부파일명")
    
    def __str__(self):
        return self.filename


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
        validators=[core_models.contents_MinLenValidator], verbose_name="내용"
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
        validators=[core_models.title_MaxLenValidator, core_models.title_MinLenValidator],
        verbose_name="제목",
    )
    contents = models.TextField(
        validators=[core_models.contents_MinLenValidator], verbose_name="내용"
    )

    viewCnts = models.PositiveIntegerField(default=0, verbose_name="조회수")

    objects = CustomManager()

    def __str__(self):
        return f"{self.title}({self.postNo})"

    def delete(self, *args, **kwargs):
        a = self.attachments.get(board=self)
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
