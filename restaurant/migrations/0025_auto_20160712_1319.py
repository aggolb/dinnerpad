# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0024_order_gps'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuextra',
            name='code',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='menuextra',
            name='description',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='category',
            field=models.CharField(blank=True, max_length=3, null=True, choices=[(b'STA', b'Starters'), (b'MAI', b'Main'), (b'DRI', b'Drinks'), (b'DES', b'Dessert'), (b'DEA', b'Deals')]),
        ),
    ]
