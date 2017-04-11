# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 22:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rewards_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Charity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('points', models.IntegerField(default=0)),
                ('mission_statement', models.CharField(blank=True, max_length=360, null=True)),
            ],
            options={
                'verbose_name_plural': 'charities',
            },
        ),
        migrations.DeleteModel(
            name='Charitiy',
        ),
    ]
