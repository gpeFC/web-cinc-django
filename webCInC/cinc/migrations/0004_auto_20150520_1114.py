# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinc', '0003_publicacion_archivo_pdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='direccionestancia',
            name='archivo_pdf',
            field=models.FileField(null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='patente',
            name='archivo_pdf',
            field=models.FileField(null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='perfildeseable',
            name='nombramiento_pdf',
            field=models.FileField(null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='premio',
            name='comprobante_pdf',
            field=models.FileField(null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='sei',
            name='archivo_pdf',
            field=models.FileField(null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='sni',
            name='nombramiento_pdf',
            field=models.FileField(null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='tesis',
            name='archivo_pdf',
            field=models.FileField(null=True, upload_to=b''),
        ),
    ]
