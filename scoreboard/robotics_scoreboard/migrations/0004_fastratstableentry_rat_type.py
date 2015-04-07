# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('robotics_scoreboard', '0003_auto_20150407_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='fastratstableentry',
            name='rat_type',
            field=models.CharField(default=b'F', max_length=12, db_column=b'Type', choices=[(b'F', b'Fast Rat'), (b'S', b'Smart Rat')]),
            preserve_default=True,
        ),
    ]
