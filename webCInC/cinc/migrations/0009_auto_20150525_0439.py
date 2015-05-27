# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinc', '0008_auto_20150522_0626'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FotoArchivo',
        ),
        migrations.AlterField(
            model_name='actaconsejotecnico',
            name='archivo_pdf',
            field=models.FileField(null=True, upload_to=b'actas-consejo-tecnico'),
        ),
        migrations.AlterField(
            model_name='actaconsejotecnico',
            name='fecha',
            field=models.CharField(max_length=9),
        ),
        migrations.AlterField(
            model_name='datosgenerales',
            name='nivel',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='direccionestancia',
            name='archivo_pdf',
            field=models.FileField(null=True, upload_to=b'direccionEstancia'),
        ),
        migrations.AlterField(
            model_name='direccionestancia',
            name='tipo',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='direccionestancia',
            name='visitante',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='patente',
            name='archivo_pdf',
            field=models.FileField(null=True, upload_to=b'patentes'),
        ),
        migrations.AlterField(
            model_name='perfildeseable',
            name='nombramiento_pdf',
            field=models.FileField(null=True, upload_to=b'perfilDeseable'),
        ),
        migrations.AlterField(
            model_name='premio',
            name='comprobante_pdf',
            field=models.FileField(null=True, upload_to=b'premios'),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='archivo_pdf',
            field=models.FileField(null=True, upload_to=b'publicaciones'),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='paginas',
            field=models.CharField(max_length=9),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='publicacion',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='sei',
            name='archivo_pdf',
            field=models.FileField(null=True, upload_to=b'sei'),
        ),
        migrations.AlterField(
            model_name='sni',
            name='nombramiento_pdf',
            field=models.FileField(null=True, upload_to=b'sni'),
        ),
        migrations.AlterField(
            model_name='tesis',
            name='archivo_pdf',
            field=models.FileField(null=True, upload_to=b'tesis'),
        ),
        migrations.AlterField(
            model_name='tesis',
            name='nivel',
            field=models.CharField(max_length=12),
        ),
    ]
