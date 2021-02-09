# Generated by Django 3.1.4 on 2021-01-04 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0003_auto_20210104_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='status',
            field=models.CharField(choices=[('4canceled', 'status_canceled'), ('3rejected', 'status_rejected'), ('5completed', 'status_completed'), ('1proposed', 'status_proposed'), ('2progress', 'status_progress')], default='1proposed', max_length=12),
        ),
    ]