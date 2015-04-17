# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('robotics_scoreboard', '0017_auto_20150417_0215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='letter_btb',
        ),
        migrations.RemoveField(
            model_name='score',
            name='number_btb',
        ),
        migrations.RemoveField(
            model_name='team',
            name='bonus_payout',
        ),
        migrations.AddField(
            model_name='score',
            name='btb_percentage',
            field=models.IntegerField(default=0, db_column=b'BTB'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='team',
            name='perfect_score_payout',
            field=models.BooleanField(default=False, db_column=b'PerfectScorePayout'),
            preserve_default=True,
        ),
    ]
