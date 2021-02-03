import os
from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from core import models as core_models

class None_Avatar(Exception):
    pass


class User(AbstractUser):

    """ Custom User Model """

    avatar = models.ImageField(blank=True, upload_to="user-files/avatars")
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


"""
# receiver이용하여 User 변경, 수정, 삭제 신호감지하여 처리 정의
@receiver(models.signals.post_delete, sender=User)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    print("딜리트")
    if instance.avatar:
        if os.path.isfile(instance.avatar.path):
            os.remove(instance.avatar.path)


# User모델 저장되기 전 가로채 함수 실행
@receiver(models.signals.pre_save, sender=User)
def auto_delete_file_on_change(sender, instance, **kwargs):
    print("수정")
    if not instance.pk:
        return False

    try:
        old_avatar = User.objects.get(pk=instance.pk).avatar

        if old_avatar == "":
            raise None_Avatar

    except None_Avatar:
        return False

    new_avatar = instance.avatar

    if not old_avatar == new_avatar:
        if os.path.isfile(old_avatar.path):
            os.remove(old_avatar.path)
"""