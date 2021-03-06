from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

title_MinLenValidator = MinLengthValidator(2, "2자 이상 입력해주세요.(2자 ~ 80자 이내)")
title_MaxLenValidator = MaxLengthValidator(80, "80자 이내로 입력해주세요.(2자 ~ 80자 이내)")
contents_MinLenValidator = MinLengthValidator(10, "글이 너무 짧습니다. 10자 이상 입력해주세요.")


class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Department(models.Model):
    class Meta:
        verbose_name = "부서"
        verbose_name_plural = "부서"

    d_id = models.PositiveIntegerField(primary_key=True, verbose_name="부서ID")
    d_name = models.CharField(max_length=80, verbose_name="부서명")

    def __str__(self):
        return self.d_name


class Position(models.Model):
    class Meta:
        verbose_name = "직급"
        verbose_name_plural = "직급"

    p_id = models.PositiveIntegerField(primary_key=True, verbose_name="직급ID")
    p_name = models.CharField(max_length=80, verbose_name="직급명")

    def __str__(self):
        return self.d_name
