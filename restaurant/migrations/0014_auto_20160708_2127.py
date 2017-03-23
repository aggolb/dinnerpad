# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0013_review_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='order',
            field=models.OneToOneField(related_name='review', null=True, blank=True, to='restaurant.Order'),
        ),
    ]
