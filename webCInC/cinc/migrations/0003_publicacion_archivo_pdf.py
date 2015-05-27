# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinc', '0002_direccionestancia_patente_perfildeseable_premio_publicacion_sei_sni_tesis'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='archivo_pdf',
            field=models.FileField(null=True, upload_to=b''),
        ),
    ]
