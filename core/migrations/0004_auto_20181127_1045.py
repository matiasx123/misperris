# Generated by Django 2.0.7 on 2018-11-27 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20181127_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='genero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Genero'),
        ),
    ]