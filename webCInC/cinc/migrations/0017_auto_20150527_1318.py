# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinc', '0016_actaconsejotecnico_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosgenerales',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='datosgenerales',
            name='foto',
            field=models.ImageField(null=True, upload_to=b'fotosInvestigadores'),
        ),
    ]
