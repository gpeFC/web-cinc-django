# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinc', '0006_fotoarchivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotoarchivo',
            name='archivo_foto',
            field=models.ImageField(upload_to=b'fotos'),
        ),
    ]
