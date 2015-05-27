# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinc', '0009_auto_20150525_0439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actaconsejotecnico',
            name='archivo_pdf',
            field=models.FileField(null=True, upload_to=b'actasConsejoTecnico'),
        ),
    ]
