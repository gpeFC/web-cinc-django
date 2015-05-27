# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinc', '0004_auto_20150520_1114'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActaConsejoTecnico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.CharField(max_length=30)),
                ('archivo_pdf', models.FileField(null=True, upload_to=b'')),
            ],
        ),
    ]
