# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-16 22:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='description',
            name='id',
        ),
        migrations.AlterField(
            model_name='description',
            name='course_desc',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Course.Course'),
        ),
    ]
