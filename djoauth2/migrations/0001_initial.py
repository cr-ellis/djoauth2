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
            name='AccessToken',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('lifetime', models.PositiveIntegerField(default=3600)),
                ('invalidated', models.BooleanField(default=False)),
                ('refreshable', models.BooleanField(default=True)),
                ('refresh_token', models.CharField(null=True, default=b'Ey5g-h-6fvlGbdUyqGElNUBiI7KBKb', max_length=30, blank=True, unique=True, db_index=True)),
                ('value', models.CharField(default=b'Q2PjAKaCJTle-oiJRprrvuOvyI775u', unique=True, max_length=30, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='AuthorizationCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('lifetime', models.PositiveIntegerField(default=600)),
                ('invalidated', models.BooleanField(default=False)),
                ('redirect_uri', models.URLField(null=True, blank=True)),
                ('value', models.CharField(default=b'~OUnCjZEuSCWil-pY032qysB2Tpnd1', unique=True, max_length=30, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(null=True, blank=True)),
                ('image_url', models.URLField(null=True, blank=True)),
                ('redirect_uri', models.URLField()),
                ('key', models.CharField(default=b'~MJiQ8viuErwMGOS8zUdqSNOqG9k4V', unique=True, max_length=30, db_index=True)),
                ('secret', models.CharField(default=b'OW6I6qGWZTj2uXuLZCqA9FLAKmKXoA', unique=True, max_length=30, db_index=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Scope',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=256, db_index=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='authorizationcode',
            name='client',
            field=models.ForeignKey(to='djoauth2.Client'),
        ),
        migrations.AddField(
            model_name='authorizationcode',
            name='scopes',
            field=models.ManyToManyField(related_name='authorization_codes', to='djoauth2.Scope'),
        ),
        migrations.AddField(
            model_name='authorizationcode',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='accesstoken',
            name='authorization_code',
            field=models.ForeignKey(related_name='access_tokens', blank=True, to='djoauth2.AuthorizationCode', null=True),
        ),
        migrations.AddField(
            model_name='accesstoken',
            name='client',
            field=models.ForeignKey(to='djoauth2.Client'),
        ),
        migrations.AddField(
            model_name='accesstoken',
            name='scopes',
            field=models.ManyToManyField(related_name='access_tokens', to='djoauth2.Scope'),
        ),
        migrations.AddField(
            model_name='accesstoken',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
