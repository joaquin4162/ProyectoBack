# Generated by Django 4.2 on 2023-06-05 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profesional', '0002_profesional_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesional',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]