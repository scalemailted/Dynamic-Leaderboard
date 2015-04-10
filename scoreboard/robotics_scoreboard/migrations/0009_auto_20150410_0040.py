# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('robotics_scoreboard', '0008_auto_20150410_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='team',
            field=models.ForeignKey(related_query_name=b'score', related_name='Scores', to='robotics_scoreboard.Team'),
            preserve_default=True,
        ),
    ]
