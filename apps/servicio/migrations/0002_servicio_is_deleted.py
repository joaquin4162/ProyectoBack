# Generated by Django 4.2 on 2023-05-09 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]