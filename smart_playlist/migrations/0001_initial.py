# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 22:52
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('spotify_id', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='AudioFeatures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Lyric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mxm_tid', models.IntegerField()),
                ('count', models.IntegerField()),
                ('is_test', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('mxm_tid', models.IntegerField()),
                ('spotify_id', models.CharField(max_length=30)),
                ('artist', models.ManyToManyField(to='smart_playlist.Artist')),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='lyric',
            name='word',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart_playlist.Word'),
        ),
        migrations.AddField(
            model_name='audiofeatures',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart_playlist.Song'),
        ),
    ]