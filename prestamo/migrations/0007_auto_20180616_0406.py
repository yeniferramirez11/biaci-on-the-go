# Generated by Django 2.0.5 on 2018-06-16 08:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestamo', '0006_auto_20180616_0351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='fecha_entrega',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 16, 4, 6, 24, 674072)),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='fecha_prestamo',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 16, 4, 6, 24, 674016)),
        ),
    ]
