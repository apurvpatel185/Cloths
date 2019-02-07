# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-28 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0003_auto_20181228_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, choices=[('jumpsuits', 'Jumpsuits'), ('traditional', 'TRADITIONAL'), ('formal', 'Formal'), ('t-shirts', 'T-shirts'), ('kids', 'Kids'), ('denim', 'Denim'), ('casual', 'Casual'), ('sports', 'Sports'), ('ethnic', 'Erhnic'), ('western', 'Western'), ('winter-wears', 'Winter-wears')], max_length=17, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='occasion',
            field=models.CharField(blank=True, choices=[('party', 'Party'), ('everyday', 'Everyday'), ('gym', 'Gym'), ('weddings', 'Weddings'), ('outings', 'Outings'), ('interview', 'Interview'), ('sangeet', 'Sangeet')], max_length=9),
        ),
    ]
