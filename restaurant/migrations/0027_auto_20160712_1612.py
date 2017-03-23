# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0026_auto_20160712_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderextra',
            name='code',
            field=models.CharField(max_length=200),
        ),
    ]
