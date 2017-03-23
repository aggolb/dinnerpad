# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurant', '0012_order_flag'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='order',
            field=models.OneToOneField(related_name='review', null=True, blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
