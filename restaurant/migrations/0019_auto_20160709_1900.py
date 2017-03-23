# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0018_auto_20160709_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuoption',
            name='description',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
