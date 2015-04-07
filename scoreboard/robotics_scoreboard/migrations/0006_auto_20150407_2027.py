# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('robotics_scoreboard', '0005_auto_20150407_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fastratstableentry',
            name='total_score',
            field=models.IntegerField(default=0, editable=False, db_column=b'Total'),
            preserve_default=True,
        ),
    ]
