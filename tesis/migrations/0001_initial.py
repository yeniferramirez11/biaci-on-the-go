# Generated by Django 2.0.5 on 2018-06-16 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('libro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tesis',
            fields=[
                ('cota', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=150)),
                ('anio', models.PositiveSmallIntegerField()),
                ('lugar_publicacion', models.TextField(max_length=50)),
                ('descripcion', models.TextField(max_length=1000)),
                ('area', models.CharField(max_length=30)),
                ('estado', models.CharField(blank=True, choices=[('P', 'Prestado'), ('D', 'Disponible'), ('B', 'Bloqueado')], default='D', max_length=1)),
                ('autor', models.ManyToManyField(to='libro.Autor')),
                ('biblioteca', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='libro.Biblioteca')),
                ('idioma', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='libro.Idioma')),
            ],
        ),
    ]
