# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import restaurant.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('price', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total', models.FloatField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('delivery', models.FloatField(default=0)),
                ('longitude', models.FloatField(default=0)),
                ('latitude', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField(default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('order', models.ForeignKey(to='restaurant.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('image', models.FileField(null=True, upload_to=restaurant.models.get_upload_file_name, blank=True)),
                ('telephone', models.CharField(max_length=200)),
                ('addressl1', models.CharField(max_length=200)),
                ('addressl2', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=10, choices=[(b'lusaka', b'Lusaka'), (b'kabwe', b'Kabwe'), (b'kitwe', b'Kitwe'), (b'ndola', b'Ndola')])),
                ('country', models.CharField(max_length=2, choices=[(b'ZM', b'Zambia')])),
                ('category', models.CharField(max_length=3, choices=[(b'PIZ', b'Pizza'), (b'SAN', b'Sandwiches'), (b'CHI', b'Chicken'), (b'GRI', b'Grill')])),
                ('date_added', models.DateField(auto_now_add=True)),
                ('rating', models.FloatField(default=0)),
                ('review_count', models.IntegerField(default=0)),
                ('order_count', models.IntegerField(default=0)),
                ('minimum_order_amount', models.FloatField(default=0)),
                ('delivery_fee', models.FloatField(default=0)),
                ('user', models.ForeignKey(related_name='restaurants', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.FloatField(default=0)),
                ('description', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('restaurant', models.ForeignKey(related_name='reviews', to='restaurant.Restaurant')),
                ('user', models.ForeignKey(related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='restaurant',
            field=models.ForeignKey(related_name='orders', to='restaurant.Restaurant'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(related_name='orders', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='restaurant',
            field=models.ForeignKey(to='restaurant.Restaurant'),
        ),
    ]
