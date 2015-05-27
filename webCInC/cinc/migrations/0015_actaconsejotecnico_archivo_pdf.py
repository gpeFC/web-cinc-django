# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinc', '0014_auto_20150525_0447'),
    ]

    operations = [
        migrations.AddField(
            model_name='actaconsejotecnico',
            name='archivo_pdf',
            field=models.FileField(null=True, upload_to=b'actasConsejoTecnico'),
        ),
    ]
