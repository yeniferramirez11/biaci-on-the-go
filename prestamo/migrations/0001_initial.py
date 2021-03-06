# Generated by Django 2.0.5 on 2018-06-26 23:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('libro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_prestamo', models.DateTimeField(default=datetime.datetime(2018, 6, 26, 19, 56, 4, 762923))),
                ('fecha_entrega', models.DateTimeField(default=datetime.datetime(2018, 6, 26, 19, 56, 4, 762977))),
                ('id_ejemplar', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='libro.Ejemplar')),
            ],
        ),
    ]
