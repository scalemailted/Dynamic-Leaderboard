# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('robotics_scoreboard', '0018_auto_20150417_0236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='penalty',
        ),
        migrations.AddField(
            model_name='score',
            name='critical_penalty',
            field=models.IntegerField(default=0, db_column=b'CriticalPenalty'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='score',
            name='search_penalty',
            field=models.IntegerField(default=0, db_column=b'SearchPenalty'),
            preserve_default=True,
        ),
    ]
