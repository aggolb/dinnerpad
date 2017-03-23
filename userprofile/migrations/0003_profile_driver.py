# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_auto_20160709_0259'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='driver',
            field=models.BooleanField(default=False),
        ),
    ]
