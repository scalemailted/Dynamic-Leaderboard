# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('robotics_scoreboard', '0004_fastratstableentry_rat_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fastratstableentry',
            name='serch_time',
        ),
        migrations.AddField(
            model_name='fastratstableentry',
            name='search_time',
            field=models.CharField(default=b'0', max_length=10, db_column=b'Search Time'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fastratstableentry',
            name='critical_time',
            field=models.CharField(default=b'0', max_length=10, db_column=b'Critical Time'),
            preserve_default=True,
        ),
    ]
