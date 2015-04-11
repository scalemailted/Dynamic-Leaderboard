# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('robotics_scoreboard', '0012_auto_20150410_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='total_score',
            field=models.IntegerField(default=0, db_column=b'TotalScore'),
            preserve_default=True,
        ),
    ]
