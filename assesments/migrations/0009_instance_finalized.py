# Generated by Django 3.2.8 on 2021-10-15 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assesments', '0008_auto_20211014_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='instance',
            name='finalized',
            field=models.BooleanField(default=False),
        ),
    ]
