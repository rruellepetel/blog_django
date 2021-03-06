# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-11 11:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20170511_1130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(blank=True)),
                ('title', models.CharField(max_length=26, unique=True)),
                ('parent_cat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='post.Category')),
            ],
        ),
    ]
