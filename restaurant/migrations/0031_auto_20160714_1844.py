# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0030_order_driver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuoption',
            name='code',
            field=models.CharField(max_length=200),
        ),
    ]
