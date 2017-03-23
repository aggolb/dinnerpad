# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstName', models.CharField(max_length=200)),
                ('lastName', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=15)),
                ('addressl1', models.CharField(max_length=200)),
                ('addressl2', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200, choices=[(b'lusaka', b'Lusaka'), (b'kabwe', b'Kabwe'), (b'kitwe', b'Kitwe'), (b'ndola', b'Ndola')])),
                ('country', models.CharField(max_length=200, choices=[(b'ZM', b'Zambia')])),
                ('user', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
