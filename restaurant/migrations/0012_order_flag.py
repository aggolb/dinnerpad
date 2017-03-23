# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0011_order_delivered'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='flag',
            field=models.BooleanField(default=False),
        ),
    ]
