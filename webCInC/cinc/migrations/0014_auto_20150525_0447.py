# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinc', '0013_auto_20150525_0445'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actaconsejotecnico',
            old_name='describe',
            new_name='fecha',
        ),
    ]
