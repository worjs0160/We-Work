from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    """ Cutom User Model """

    avatar = models.ImageField(blank=True)
    user_name = models.CharField(max_length=15, verbose_name="이름")
    user_position = models.CharField(
        default="position", max_length=15, verbose_name="직급"
    )
    phone_num = models.CharField(max_length=15, verbose_name="전화번호")
    user_addr = models.CharField(max_length=15, verbose_name="주소")
    post_num = models.IntegerField(blank=True, verbose_name="우편번호")
    birthdate = models.DateField(blank=True, null=True, verbose_name="생년월일")
    user_bio = models.TextField(blank=True, verbose_name="유저정보")
    is_cert = models.BooleanField(default=False, verbose_name="인증여부")

    def __str__(self):
        return f"{self.user_name}({self.username})"
