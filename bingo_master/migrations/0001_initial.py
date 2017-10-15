# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-15 23:55
from __future__ import unicode_literals

import bingo_master.validators
import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BingoBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(verbose_name='game start datetime')),
                ('end_date', models.DateTimeField(verbose_name='game end datetime')),
                ('board', django.contrib.postgres.fields.ArrayField(base_field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(75)]), size=75, validators=[bingo_master.validators.DuplicateValidator()])),
            ],
        ),
    ]
