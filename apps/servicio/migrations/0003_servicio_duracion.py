# Generated by Django 4.2 on 2023-05-16 00:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0002_servicio_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='duracion',
            field=models.DurationField(default=datetime.timedelta(seconds=1800)),
        ),
    ]