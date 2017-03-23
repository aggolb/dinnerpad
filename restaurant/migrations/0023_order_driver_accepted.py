# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0022_auto_20160710_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='driver_accepted',
            field=models.BooleanField(default=False),
        ),
    ]
