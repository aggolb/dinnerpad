# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0025_auto_20160712_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderextra',
            name='description',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
