# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinc', '0012_actaconsejotecnico'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actaconsejotecnico',
            old_name='fecha',
            new_name='describe',
        ),
    ]
