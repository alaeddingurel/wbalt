# Generated by Django 2.1 on 2018-08-13 07:57

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classify', '0020_auto_20180813_0751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textfile',
            name='info',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'baglan': None, 'balacan': None, 'cagri': None}),
        ),
    ]