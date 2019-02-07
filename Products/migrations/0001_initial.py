# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-22 06:02
from __future__ import unicode_literals

import Products.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Home', '0004_auto_20181222_1029'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, default='99.99', max_digits=10)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('category', models.CharField(blank=True, choices=[('ethnic', 'Erhnic'), ('kids', 'Kids'), ('t-shirts', 'T-shirts'), ('winter-wears', 'Winter-wears'), ('casual', 'Casual'), ('jumpsuits', 'Jumpsuits'), ('denim', 'Denim'), ('sports', 'Sports'), ('western', 'Western'), ('formal', 'Formal'), ('traditional', 'TRADITIONAL')], max_length=17, null=True)),
                ('occasion', models.CharField(blank=True, choices=[('interview', 'Interview'), ('gym', 'Gym'), ('outings', 'Outings'), ('everyday', 'Everyday'), ('weddings', 'Weddings'), ('sangeet', 'Sangeet'), ('party', 'Party')], max_length=9)),
                ('available', models.BooleanField(default=True)),
                ('stock', models.PositiveIntegerField()),
                ('featured', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('sold', models.BooleanField(default=False)),
                ('image1', models.ImageField(upload_to=Products.models.upload_image_path)),
                ('image2', models.ImageField(blank=True, null=True, upload_to=Products.models.upload_image_path)),
                ('image3', models.ImageField(blank=True, null=True, upload_to=Products.models.upload_image_path)),
                ('image4', models.ImageField(blank=True, null=True, upload_to=Products.models.upload_image_path)),
                ('img', models.ImageField(blank=True, upload_to=Products.models.upload_image_path)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Home.Profile')),
            ],
            options={
                'db_table': 'Product',
            },
        ),
    ]