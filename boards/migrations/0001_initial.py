# Generated by Django 3.1.4 on 2021-01-03 13:12

import ckeditor_uploader.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('postNo', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='게시물 번호')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=80, validators=[django.core.validators.MaxLengthValidator(80, '80자 이내로 입력해주세요.(2자 ~ 80자 이내)'), django.core.validators.MinLengthValidator(2, '2자 이상 입력해주세요.(2자 ~ 80자 이내)')], verbose_name='제목')),
                ('contents', ckeditor_uploader.fields.RichTextUploadingField(validators=[django.core.validators.MinLengthValidator(10, '글이 너무 짧습니다. 10자 이상 입력해주세요.')], verbose_name='내용')),
                ('viewCnts', models.PositiveIntegerField(default=0, verbose_name='조회수')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boards', to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
            options={
                'verbose_name': '공지사항',
                'verbose_name_plural': '공지사항',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('contents', models.TextField(validators=[django.core.validators.MinLengthValidator(10, '글이 너무 짧습니다. 10자 이상 입력해주세요.')], verbose_name='내용')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boards', to='boards.board', verbose_name='게시글')),
            ],
            options={
                'verbose_name': '댓글',
                'verbose_name_plural': '댓글',
            },
        ),
    ]
