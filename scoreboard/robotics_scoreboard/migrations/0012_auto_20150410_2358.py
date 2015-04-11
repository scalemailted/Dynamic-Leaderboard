# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('robotics_scoreboard', '0011_auto_20150410_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='disqualified',
            field=models.BooleanField(default=False, db_column=b'Disqualified'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='team',
            name='in_final',
            field=models.BooleanField(default=True, db_column=b'InFinal'),
            preserve_default=True,
        ),
    ]
