# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_auto_20160707_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='saturday_close',
            field=models.CharField(default=b'20:00', max_length=4, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='saturday_open',
            field=models.CharField(default=b'09:00', max_length=4, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='sunday_close',
            field=models.CharField(default=b'20:00', max_length=4, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='sunday_open',
            field=models.CharField(default=b'09:00', max_length=4, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='weekday_close',
            field=models.CharField(default=b'20:00', max_length=4, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='weekday_open',
            field=models.CharField(default=b'09:00', max_length=4, null=True, blank=True),
        ),
    ]
