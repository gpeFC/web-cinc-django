# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DireccionEstancia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=30)),
                ('visitante', models.CharField(max_length=30)),
                ('duracion', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Patente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('anio', models.CharField(max_length=4)),
                ('referencia', models.TextField()),
                ('pitc_s', models.TextField()),
                ('estatus', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='PerfilDeseable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vigencia', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Premio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('anio', models.CharField(max_length=4)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('anio', models.CharField(max_length=4)),
                ('tipo', models.CharField(max_length=30)),
                ('indizada_jcr', models.CharField(max_length=2)),
                ('con_alumnos', models.CharField(max_length=2)),
                ('titulo', models.CharField(max_length=150)),
                ('autores', models.TextField()),
                ('publicacion', models.CharField(max_length=30)),
                ('volumen', models.IntegerField()),
                ('numero', models.IntegerField()),
                ('paginas', models.CharField(max_length=30)),
                ('issn_isbn', models.CharField(max_length=30)),
                ('doi', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SEI',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tiene', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='SNI',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nivel', models.CharField(max_length=3)),
                ('vigencia', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Tesis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('anio', models.CharField(max_length=4)),
                ('nivel', models.CharField(max_length=11)),
            ],
        ),
    ]
