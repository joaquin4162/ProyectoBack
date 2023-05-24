# Generated by Django 4.2 on 2023-05-16 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('servicio', '0003_servicio_duracion'),
        ('profesional', '0002_remove_profesional_servicio_profesional_is_deleted'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfesionalServicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_borrado', models.DateField()),
                ('profesional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profesional.profesional')),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicio.servicio')),
            ],
        ),
    ]
