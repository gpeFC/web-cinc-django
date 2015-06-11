# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActaConsejoTecnico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.CharField(default=b'DD/MM/AAAA', max_length=10)),
                ('numero', models.IntegerField(null=True)),
                ('archivo_pdf', models.FileField(null=True, upload_to=b'actasConsejoTecnico')),
            ],
        ),
        migrations.CreateModel(
            name='DatosGenerales',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=75)),
                ('nivel', models.CharField(max_length=10)),
                ('definitivo', models.CharField(max_length=2)),
                ('fecha_ingreso_uaem', models.CharField(max_length=4)),
                ('departamento', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('foto', models.ImageField(null=True, upload_to=b'fotosInvestigadores')),
            ],
        ),
        migrations.CreateModel(
            name='DireccionEstancia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=12)),
                ('visitante', models.CharField(max_length=2)),
                ('duracion', models.CharField(max_length=9)),
                ('archivo_pdf', models.FileField(null=True, upload_to=b'direccionEstancia')),
            ],
        ),
        migrations.CreateModel(
            name='Patente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('anio', models.CharField(max_length=4)),
                ('referencia', models.TextField()),
                ('pitc_s', models.TextField()),
                ('estatus', models.CharField(max_length=10)),
                ('archivo_pdf', models.FileField(null=True, upload_to=b'patentes')),
            ],
        ),
        migrations.CreateModel(
            name='PerfilDeseable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vigencia', models.CharField(max_length=9)),
                ('nombramiento_pdf', models.FileField(null=True, upload_to=b'perfilDeseable')),
            ],
        ),
        migrations.CreateModel(
            name='Premio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('anio', models.CharField(max_length=4)),
                ('descripcion', models.TextField()),
                ('comprobante_pdf', models.FileField(null=True, upload_to=b'premios')),
            ],
        ),
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('anio', models.CharField(max_length=4)),
                ('tipo', models.CharField(max_length=30)),
                ('indizada_jcr', models.CharField(max_length=2)),
                ('con_alumnos', models.CharField(max_length=2)),
                ('titulo', models.CharField(max_length=150)),
                ('autores', models.TextField()),
                ('publicacion', models.CharField(max_length=8)),
                ('volumen', models.IntegerField()),
                ('numero', models.IntegerField()),
                ('paginas', models.CharField(max_length=9)),
                ('issn_isbn', models.CharField(max_length=30)),
                ('doi', models.CharField(max_length=50)),
                ('archivo_pdf', models.FileField(null=True, upload_to=b'publicaciones')),
            ],
        ),
        migrations.CreateModel(
            name='SEI',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tiene', models.CharField(max_length=2)),
                ('archivo_pdf', models.FileField(null=True, upload_to=b'sei')),
            ],
        ),
        migrations.CreateModel(
            name='SNI',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nivel', models.CharField(max_length=3)),
                ('vigencia', models.CharField(max_length=9)),
                ('nombramiento_pdf', models.FileField(null=True, upload_to=b'sni')),
            ],
        ),
        migrations.CreateModel(
            name='Tesis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('anio', models.CharField(max_length=4)),
                ('nivel', models.CharField(max_length=12)),
                ('archivo_pdf', models.FileField(null=True, upload_to=b'tesis')),
            ],
        ),
    ]
