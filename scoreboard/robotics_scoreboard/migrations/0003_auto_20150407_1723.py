# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('robotics_scoreboard', '0002_fastratstableentry_smartratstableentry'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SmartRatsTableEntry',
        ),
        migrations.RemoveField(
            model_name='fastratstableentry',
            name='critical',
        ),
        migrations.RemoveField(
            model_name='fastratstableentry',
            name='search',
        ),
        migrations.RemoveField(
            model_name='fastratstableentry',
            name='time',
        ),
        migrations.RemoveField(
            model_name='fastratstableentry',
            name='total',
        ),
        migrations.AddField(
            model_name='fastratstableentry',
            name='critical_path',
            field=models.IntegerField(default=0, db_column=b'Critical Path'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fastratstableentry',
            name='critical_time',
            field=models.CharField(default=b'', max_length=10, db_column=b'Critical Time'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fastratstableentry',
            name='easter_egg',
            field=models.IntegerField(default=0, db_column=b'Easter Egg'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fastratstableentry',
            name='round_score',
            field=models.IntegerField(default=0, db_column=b'Round'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fastratstableentry',
            name='search_path',
            field=models.IntegerField(default=0, db_column=b'Search Path'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fastratstableentry',
            name='serch_time',
            field=models.CharField(default=b'', max_length=10, db_column=b'Search Time'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fastratstableentry',
            name='total_score',
            field=models.IntegerField(default=0, db_column=b'Total'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fastratstableentry',
            name='penalty',
            field=models.IntegerField(default=0, db_column=b'Penalty'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fastratstableentry',
            name='team',
            field=models.CharField(unique=True, max_length=10, db_column=b'Team'),
            preserve_default=True,
        ),
    ]
