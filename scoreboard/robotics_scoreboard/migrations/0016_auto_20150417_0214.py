# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('robotics_scoreboard', '0015_auto_20150414_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='letter_btb',
            field=models.DecimalField(default=0.0, decimal_places=2, max_digits=3, db_column=b'LBT'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='score',
            name='number_btb',
            field=models.DecimalField(default=0.0, decimal_places=2, max_digits=3, db_column=b'NBT'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='team',
            name='get_bonus',
            field=models.BooleanField(default=False, db_column=b'GetBonus'),
            preserve_default=True,
        ),
    ]
