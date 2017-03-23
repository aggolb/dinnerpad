# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_auto_20160713_2147'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='reffered_by',
            new_name='referred_by',
        ),
    ]
