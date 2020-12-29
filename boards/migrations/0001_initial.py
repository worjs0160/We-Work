# Generated by Django 3.1.4 on 2020-12-29 08:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('postNo', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='게시물 번호')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=80, validators=[django.core.validators.MaxLengthValidator(80, '80자 이내로 입력해주세요(2자 ~ 80자 이내)'), django.core.validators.MinLengthValidator(2, '2자 이상 입력해주세요(2자 ~ 80자 이내)')], verbose_name='제목')),
                ('contents', models.TextField(blank=True, verbose_name='내용')),
                ('viewCnts', models.PositiveIntegerField(default=0, verbose_name='조회수')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boards', to='users.user', verbose_name='작성자')),
            ],
            options={
                'verbose_name': '공지사항',
                'verbose_name_plural': '공지사항',
            },
        ),
    ]
