# Generated by Django 2.0.7 on 2018-07-27 11:47

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classify', '0018_auto_20180727_0944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='textfile',
            name='newuser',
        ),
        migrations.RemoveField(
            model_name='textfile',
            name='user',
        ),
        migrations.AddField(
            model_name='textfile',
            name='info',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'newuser': False, 'user': False}),
        ),
    ]
