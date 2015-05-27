# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinc', '0007_auto_20150522_0559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actaconsejotecnico',
            name='archivo_pdf',
            field=models.FileField(null=True, upload_to=b'pdfs'),
        ),
        migrations.AlterField(
            model_name='direccionestancia',
            name='archivo_pdf',
            field=models.FileField(null=True, upload_to=b'pdfs'),
        ),
        migrations.AlterField(
            model_name='patente',
            name='archivo_pdf',
            field=models.FileField(null=True, upload_to=b'pdfs'),
        ),
        migrations.AlterField(
            model_name='perfildeseable',
            name='nombramiento_pdf',
            field=models.FileField(null=True, upload_to=b'pdfs'),
        ),
        migrations.AlterField(
            model_name='premio',
            name='comprobante_pdf',
            field=models.FileField(null=True, upload_to=b'pdfs'),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='archivo_pdf',
            field=models.FileField(null=True, upload_to=b'pdfs'),
        ),
        migrations.AlterField(
            model_name='sei',
            name='archivo_pdf',
            field=models.FileField(null=True, upload_to=b'pdfs'),
        ),
        migrations.AlterField(
            model_name='sni',
            name='nombramiento_pdf',
            field=models.FileField(null=True, upload_to=b'pdfs'),
        ),
        migrations.AlterField(
            model_name='tesis',
            name='archivo_pdf',
            field=models.FileField(null=True, upload_to=b'pdfs'),
        ),
    ]
