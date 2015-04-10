# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('robotics_scoreboard', '0007_auto_20150407_2043'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('round', models.CharField(default=1, max_length=5, db_column=b'Round', choices=[(b'1', b'One'), (b'2', b'Two'), (b'3', b'Three'), (b'F', b'Final')])),
                ('search_path', models.IntegerField(default=0, db_column=b'Search Path')),
                ('search_time', models.CharField(default=b'0', max_length=10, db_column=b'Search Time')),
                ('critical_path', models.IntegerField(default=0, db_column=b'Critical Path')),
                ('critical_time', models.CharField(default=b'0', max_length=10, db_column=b'Critical Time')),
                ('easter_egg', models.IntegerField(default=0, db_column=b'Easter Egg')),
                ('penalty', models.IntegerField(default=0, db_column=b'Penalty')),
                ('round_score', models.IntegerField(default=0, editable=False, db_column=b'Round Score')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('team_name', models.CharField(unique=True, max_length=10, db_column=b'Team')),
                ('team_number', models.IntegerField(default=0, unique=True, db_column=b'#')),
                ('rat_type', models.CharField(default=b'F', max_length=12, db_column=b'Type', choices=[(b'F', b'Fast Rat'), (b'S', b'Smart Rat')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='score',
            name='team',
            field=models.ForeignKey(related_name='Scores', to='robotics_scoreboard.Team'),
            preserve_default=True,
        ),
    ]
