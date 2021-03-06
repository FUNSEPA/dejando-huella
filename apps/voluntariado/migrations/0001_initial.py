# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-09 14:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import easy_thumbnails.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('grado', models.CharField(max_length=30)),
                ('fecha_nacimiento', models.DateField()),
                ('grande', models.CharField(max_length=150)),
                ('sobre', models.TextField()),
                ('color', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Historia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('subtitulo', models.CharField(max_length=200)),
                ('portada', easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to='historia_media')),
            ],
            options={
                'verbose_name': 'Historia',
                'verbose_name_plural': 'Historias',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=140)),
                ('texto', models.TextField()),
                ('orden', models.PositiveIntegerField()),
                ('fondo', easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to='post_media')),
                ('imagen', easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to='post_media')),
                ('video', models.TextField(blank=True, null=True)),
                ('historia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voluntariado.Historia')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
