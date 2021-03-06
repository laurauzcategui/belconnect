# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-10 16:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BelMeeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('datetime', models.DateTimeField(blank=True, default=9999)),
                ('topic', models.CharField(default=0, max_length=200)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='BelStop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('location', models.CharField(max_length=200)),
                ('spots_available', models.IntegerField(default=0)),
                ('times_available', models.CommaSeparatedIntegerField(default=0, max_length=200)),
                ('accepts_belPoints', models.BooleanField(default=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='belstops', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.AddField(
            model_name='belmeeting',
            name='belStop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.BelStop'),
        ),
        migrations.AddField(
            model_name='belmeeting',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='belmeetings', to=settings.AUTH_USER_MODEL),
        ),
    ]
