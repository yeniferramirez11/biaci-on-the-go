# Generated by Django 2.0.5 on 2018-06-13 14:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestamo', '0011_auto_20180612_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='fecha_entrega',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 13, 10, 47, 57, 611619)),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='fecha_prestamo',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 13, 10, 47, 57, 611565)),
        ),
    ]
