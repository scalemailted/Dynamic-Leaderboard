# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('robotics_scoreboard', '0013_team_total_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='critical_time',
            field=models.DecimalField(default=0.0, decimal_places=1, max_digits=10, db_column=b'CriticalTime'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='score',
            name='search_time',
            field=models.DecimalField(default=0.0, decimal_places=1, max_digits=10, db_column=b'SearchTime'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='team',
            name='in_final',
            field=models.BooleanField(default=False, db_column=b'InFinal'),
            preserve_default=True,
        ),
    ]
