# Generated by Django 2.0.7 on 2018-07-19 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classify', '0007_remove_annotator_text_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='annotator',
            name='annotext',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='classify.TextFile'),
            preserve_default=False,
        ),
    ]