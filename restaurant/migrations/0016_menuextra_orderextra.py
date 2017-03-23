# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0015_orderitem_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuExtra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=200)),
                ('price', models.FloatField(default=0)),
                ('item', models.ForeignKey(related_name='extras', to='restaurant.MenuItem')),
            ],
        ),
        migrations.CreateModel(
            name='OrderExtra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=200)),
                ('price', models.FloatField(default=0)),
                ('order_item', models.ForeignKey(related_name='order_item_extras', to='restaurant.OrderItem')),
            ],
        ),
    ]
