# Generated by Django 2.0.7 on 2018-07-24 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classify', '0012_auto_20180724_1155'),
    ]

    operations = [
        migrations.RenameField(
            model_name='textfile',
            old_name='json_var',
            new_name='info',
        ),
    ]