# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatosGenerales',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=75)),
                ('nivel', models.CharField(max_length=30)),
                ('definitivo', models.CharField(max_length=2)),
                ('fecha_ingreso_uaem', models.CharField(max_length=4)),
                ('departamento', models.CharField(max_length=11)),
            ],
        ),
    ]
