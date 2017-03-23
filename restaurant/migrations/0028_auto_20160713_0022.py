# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0027_auto_20160712_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='description',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
