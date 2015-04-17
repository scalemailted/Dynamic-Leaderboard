# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('robotics_scoreboard', '0016_auto_20150417_0214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='get_bonus',
        ),
        migrations.AddField(
            model_name='team',
            name='bonus_payout',
            field=models.BooleanField(default=False, db_column=b'BonusPayout'),
            preserve_default=True,
        ),
    ]
