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
            name='Referral',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activated', models.BooleanField(default=False)),
                ('user1', models.ForeignKey(related_name='referrals', to=settings.AUTH_USER_MODEL)),
                ('user2', models.OneToOneField(related_name='referred_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
