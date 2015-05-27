# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinc', '0015_actaconsejotecnico_archivo_pdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='actaconsejotecnico',
            name='descripcion',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
