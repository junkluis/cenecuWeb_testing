# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-29 19:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anuncio',
            old_name='fecha_caducidad',
            new_name='fecha_limite',
        ),
        migrations.RemoveField(
            model_name='anuncio',
            name='url_anuncio',
        ),
    ]
