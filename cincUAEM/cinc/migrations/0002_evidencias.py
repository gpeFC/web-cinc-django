# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evidencias',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=30)),
                ('fecha', models.DateField()),
                ('descripcion', models.CharField(max_length=150)),
                ('imagen', models.ImageField(upload_to=b'imagenesEvidencias')),
                ('link_video', models.CharField(max_length=500, null=True)),
                ('archivo_pdf', models.FileField(null=True, upload_to=b'archivosEvidencias')),
            ],
        ),
    ]
