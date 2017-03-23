# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_auto_20160707_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='category',
            field=models.CharField(blank=True, max_length=3, null=True, choices=[(b'STA', b'Starters'), (b'MAI', b'Main'), (b'DRI', b'Drinks'), (b'DES', b'Dessert')]),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='restaurant',
            field=models.ForeignKey(related_name='menu_items', to='restaurant.Restaurant'),
        ),
    ]
