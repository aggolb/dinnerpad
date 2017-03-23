# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0016_menuextra_orderextra'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuOption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=200)),
                ('price', models.FloatField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='menuitem',
            name='variations',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='orderextra',
            name='order_item',
            field=models.ForeignKey(related_name='order_extras', to='restaurant.OrderItem'),
        ),
        migrations.AddField(
            model_name='menuoption',
            name='item',
            field=models.ForeignKey(related_name='options', to='restaurant.MenuItem'),
        ),
    ]
