# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinc', '0002_evidencias'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
                ('descripcion', models.CharField(max_length=500)),
                ('imagen', models.ImageField(null=True, upload_to=b'imagenesActividades')),
                ('link', models.CharField(max_length=500, null=True)),
                ('archivo_pdf', models.FileField(null=True, upload_to=b'archivosActividades')),
            ],
        ),
        migrations.CreateModel(
            name='Aviso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
                ('descripcion', models.CharField(max_length=500)),
                ('link', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Evidencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
                ('descripcion', models.CharField(max_length=500)),
                ('imagen', models.ImageField(upload_to=b'imagenesEvidencias')),
                ('link_video', models.CharField(max_length=500, null=True)),
                ('archivo_pdf', models.FileField(null=True, upload_to=b'archivosEvidencias')),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
                ('link', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Miscelaneo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
                ('descripcion', models.CharField(max_length=500)),
                ('imagen', models.ImageField(null=True, upload_to=b'imagenesMiscelaneos')),
                ('link', models.CharField(max_length=500, null=True)),
                ('archivo_pdf', models.FileField(null=True, upload_to=b'archivosMiscelaneos')),
            ],
        ),
        migrations.DeleteModel(
            name='Evidencias',
        ),
    ]
