# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-28 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rentit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.DecimalField(decimal_places=2, max_digits=20, max_length=20)),
            ],
        ),
    ]
