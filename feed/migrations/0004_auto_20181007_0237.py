# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-10-07 02:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_auto_20181007_0233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('DV', 'development'), ('PN', 'pensonal'), ('TV', 'travel')], default='DV', max_length=2),
        ),
    ]
