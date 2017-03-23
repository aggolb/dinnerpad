# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0017_auto_20160709_1810'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuOptionValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=200)),
                ('price', models.FloatField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='menuoption',
            name='price',
        ),
        migrations.AlterField(
            model_name='menuoption',
            name='item',
            field=models.ForeignKey(related_name='properties', to='restaurant.MenuItem'),
        ),
        migrations.AddField(
            model_name='menuoptionvalue',
            name='option',
            field=models.ForeignKey(related_name='values', to='restaurant.MenuOption'),
        ),
    ]
