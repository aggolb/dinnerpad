# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_profile_driver'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='first_purchase',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='referral_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='reffered_by',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
