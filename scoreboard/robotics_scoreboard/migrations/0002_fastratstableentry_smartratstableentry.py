# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('robotics_scoreboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FastRatsTableEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('team', models.CharField(unique=True, max_length=10)),
                ('search', models.IntegerField(default=0)),
                ('critical', models.IntegerField(default=0)),
                ('time', models.IntegerField(default=0)),
                ('penalty', models.IntegerField(default=0)),
                ('total', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SmartRatsTableEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('team', models.CharField(unique=True, max_length=10)),
                ('search', models.IntegerField(default=0)),
                ('critical', models.IntegerField(default=0)),
                ('time', models.IntegerField(default=0)),
                ('easter_egg', models.IntegerField(default=0)),
                ('penalty', models.IntegerField(default=0)),
                ('total', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
