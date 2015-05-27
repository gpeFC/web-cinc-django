# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinc', '0011_delete_actaconsejotecnico'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActaConsejoTecnico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.CharField(max_length=9)),
            ],
        ),
    ]
