# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('robotics_scoreboard', '0010_auto_20150410_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='team_number',
            field=models.IntegerField(default=0, unique=True, db_column=b'TeamNumber'),
            preserve_default=True,
        ),
    ]
