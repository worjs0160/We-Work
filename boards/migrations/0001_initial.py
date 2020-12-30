# Generated by Django 3.1.4 on 2020-12-29 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('postNo', models.CharField(blank=True, max_length=8, verbose_name='게시물 번호')),
                ('title', models.CharField(blank=True, max_length=200, verbose_name='제목')),
                ('contents', models.TextField(blank=True, verbose_name='내용')),
                ('viewCnts', models.PositiveIntegerField(default=0, verbose_name='조회수')),
            ],
            options={
                'verbose_name': '공지사항',
                'verbose_name_plural': '공지사항',
            },
        ),
    ]