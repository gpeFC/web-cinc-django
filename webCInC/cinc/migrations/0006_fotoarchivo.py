# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinc', '0005_actaconsejotecnico'),
    ]

    operations = [
        migrations.CreateModel(
            name='FotoArchivo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=140)),
                ('archivo_foto', models.ImageField(upload_to=b'')),
            ],
        ),
    ]
