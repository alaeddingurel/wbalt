# Generated by Django 2.0.7 on 2018-07-27 09:19

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classify', '0016_auto_20180727_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textfile',
            name='info',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'newuserisprotest': False, 'userisprotest': False}),
        ),
    ]
