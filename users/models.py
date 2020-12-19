from django.db import models


class User(models.Model):

    """ Cutom User Model """

    avatar = models.ImageField(blank=True)
    user_id = models.CharField(max_length=15)
    user_pw = models.CharField(max_length=15)
    user_name = models.CharField(default="test", max_length=15)
    user_email = models.CharField(default="email", max_length=15)
    user_position = models.CharField(default="position", max_length=15)
    birthdate = models.DateField(auto_now=True)
    user_bio = models.TextField(blank=True)
    phone_num = models.CharField(default="010", max_length=15)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    user_addr = models.CharField(default="addr", max_length=15)
    post_num = models.IntegerField(default=00000)
    is_cert = models.BooleanField(default=False)
