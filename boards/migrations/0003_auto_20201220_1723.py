# Generated by Django 3.1.4 on 2020-12-20 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_auto_20201220_1720'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='board',
            options={'verbose_name': '공지사항', 'verbose_name_plural': '공지사항'},
        ),
    ]
