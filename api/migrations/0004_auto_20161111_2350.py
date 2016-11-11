# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-11 23:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20161111_2324'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='item',
            unique_together=set([('code', 'client')]),
        ),
        migrations.AlterIndexTogether(
            name='item',
            index_together=set([('code', 'client')]),
        ),
    ]
