# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0009_order_expiry_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='placed',
            field=models.BooleanField(default=False),
        ),
    ]
