# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0028_auto_20160713_0022'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuextra',
            name='price_adjusted',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='price_adjusted',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='menuoptionvalue',
            name='price_adjusted',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='orderextra',
            name='price_adjusted',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='price_adjusted',
            field=models.FloatField(default=0),
        ),
    ]
