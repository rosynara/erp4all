# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-15 19:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='marca_id',
            new_name='marca',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='unidade_id',
            new_name='unidade',
        ),
        migrations.RenameField(
            model_name='itemmov',
            old_name='item_id',
            new_name='item',
        ),
        migrations.RenameField(
            model_name='itemmov',
            old_name='local_id',
            new_name='local',
        ),
        migrations.RenameField(
            model_name='itemmov',
            old_name='pessoa_id',
            new_name='pessoa',
        ),
    ]
