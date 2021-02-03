from django.db import models
from django.contrib.auth.models import AbstractUser
from core import models as core_models

class User(AbstractUser):

    """ Custom User Model """

    avatar = models.ImageField(blank=True)
    user_name = models.CharField(max_length=15, verbose_name="이름")
    phone_num = models.CharField(max_length=15, verbose_name="전화번호")
    user_addr = models.CharField(max_length=15, verbose_name="주소")
    post_num = models.IntegerField(blank=True, null=True, verbose_name="우편번호")

    birthdate = models.DateField(blank=True, null=True, verbose_name="생년월일")
    user_bio = models.TextField(blank=True, verbose_name="유저정보")
    is_cert = models.BooleanField(default=False, verbose_name="유저인증")

    position = models.OneToOneField("core.Position",related_name="user", on_delete=models.DO_NOTHING, null=True)
    department = models.OneToOneField("core.Department",related_name="user", on_delete=models.DO_NOTHING, null=True)
    
    def __str__(self):
        return f"{self.user_name}({self.username})"