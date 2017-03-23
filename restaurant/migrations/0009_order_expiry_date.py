# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0008_auto_20160708_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='expiry_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
