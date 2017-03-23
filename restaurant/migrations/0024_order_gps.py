# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0023_order_driver_accepted'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='gps',
            field=models.BooleanField(default=True),
        ),
    ]
