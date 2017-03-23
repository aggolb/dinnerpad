# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurant', '0029_auto_20160713_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='driver',
            field=models.ForeignKey(related_name='deliveries', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
