# Generated by Django 2.0.5 on 2018-06-03 19:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0006_auto_20180603_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='fecha_caducidad',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 4, 1, 33, 33, 381461)),
        ),
    ]
