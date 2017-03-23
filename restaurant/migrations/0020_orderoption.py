# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0019_auto_20160709_1900'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderOption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=200)),
                ('order_item', models.ForeignKey(related_name='order_options', to='restaurant.OrderItem')),
            ],
        ),
    ]
