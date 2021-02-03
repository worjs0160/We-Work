from django.db import models
from core.models import TimeStampedModel, title_MaxLenValidator, title_MinLenValidator, contents_MinLenValidator
# Create your models here.

class DocBase(TimeStampedModel):
    """
        결재서류 Base 클래스(공통내용)
    """
    author = models.ForeignKey("users.User", related_name="%(class)s".lower(), on_delete=models.CASCADE)
    title = models.CharField(
        max_length=80,
        validators=[title_MaxLenValidator, title_MinLenValidator],
        verbose_name="제목",
    )
    contents = models.TextField(
        validators=[contents_MinLenValidator], verbose_name="내용"
    )

    class Meta:
        abstract = True


class Draft(DocBase):
    """
    기안서 클래스
    """
    #meet_date = models.DateField() #회의일시
    pass
    
class Meeting(DocBase):
    """
    회의보고서
    """
    pass

class Business(DocBase):
    """
    업무보고서
    """
    pass

class Result(DocBase):
    """
    결과보고서
    """
    pass

class Voucher(DocBase):
    """
    지출결의서
    """
    pass

