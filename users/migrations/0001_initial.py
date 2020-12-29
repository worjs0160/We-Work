# Generated by Django 3.1.4 on 2020-12-29 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('avatar', models.ImageField(blank=True, upload_to='')),
                ('user_id', models.CharField(max_length=15)),
                ('user_pw', models.CharField(max_length=15)),
                ('user_name', models.CharField(default='test', max_length=15)),
                ('user_email', models.CharField(default='email', max_length=15)),
                ('user_position', models.CharField(default='position', max_length=15)),
                ('birthdate', models.DateField(auto_now=True)),
                ('user_bio', models.TextField(blank=True)),
                ('phone_num', models.CharField(default='010', max_length=15)),
                ('user_addr', models.CharField(default='addr', max_length=15)),
                ('post_num', models.IntegerField(default=0)),
                ('is_cert', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
