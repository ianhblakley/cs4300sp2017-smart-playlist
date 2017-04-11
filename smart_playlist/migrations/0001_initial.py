# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-04-11 20:34
from __future__ import unicode_literals

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('mxm_id', models.IntegerField(null=True, unique=True)),
                ('spotify_id', models.CharField(max_length=30, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('mxm_id', models.IntegerField(null=True, unique=True)),
                ('spotify_id', models.CharField(max_length=30, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='AudioFeatures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('danceability', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0),
                                                               django.core.validators.MaxValueValidator(1.0)])),
                ('energy', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0),
                                                         django.core.validators.MaxValueValidator(1.0)])),
                ('key', models.IntegerField(
                    choices=[(0, b'C'), (1, b'C#'), (2, b'D'), (3, b'D#'), (4, b'E'), (5, b'F'), (6, b'F#'), (7, b'G'),
                             (8, b'G#'), (9, b'A'), (10, b'A#'), (11, b'B')])),
                ('loudness', models.FloatField()),
                ('mode', models.IntegerField(choices=[(0, b'Major'), (1, b'Minor')])),
                ('speechiness', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0),
                                                              django.core.validators.MaxValueValidator(1.0)])),
                ('acousticness', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0),
                                                               django.core.validators.MaxValueValidator(1.0)])),
                ('instrumentalness', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0),
                                                                   django.core.validators.MaxValueValidator(1.0)])),
                ('liveness', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0),
                                                           django.core.validators.MaxValueValidator(1.0)])),
                ('valence', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0),
                                                          django.core.validators.MaxValueValidator(1.0)])),
                ('tempo', models.FloatField()),
                ('duration_ms', models.IntegerField()),
                ('time_signature', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Lyric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mxm_id', models.IntegerField()),
                ('count', models.IntegerField()),
                ('is_test', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('mxm_tid', models.IntegerField(null=True, unique=True)),
                ('spotify_id', models.CharField(max_length=30, null=True, unique=True)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart_playlist.Album')),
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
            name='song',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='smart_playlist.Song'),
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
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart_playlist.Artist'),
        ),
    ]
