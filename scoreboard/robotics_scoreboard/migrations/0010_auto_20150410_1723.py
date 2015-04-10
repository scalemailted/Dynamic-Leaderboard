# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('robotics_scoreboard', '0009_auto_20150410_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='critical_path',
            field=models.IntegerField(default=0, db_column=b'CriticalPath'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='score',
            name='critical_time',
            field=models.CharField(default=b'0', max_length=10, db_column=b'CriticalTime'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='score',
            name='easter_egg',
            field=models.IntegerField(default=0, db_column=b'EasterEgg'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='score',
            name='round_score',
            field=models.IntegerField(default=0, editable=False, db_column=b'RoundScore'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='score',
            name='search_path',
            field=models.IntegerField(default=0, db_column=b'SearchPath'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='score',
            name='search_time',
            field=models.CharField(default=b'0', max_length=10, db_column=b'SearchTime'),
            preserve_default=True,
        ),
    ]
