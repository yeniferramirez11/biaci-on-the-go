# Generated by Django 2.0.5 on 2018-05-29 02:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0002_auto_20180528_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='fecha_caducidad',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 29, 8, 32, 42, 684343)),
        ),
    ]
