# Generated by Django 3.2.8 on 2021-10-14 20:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('assesments', '0006_auto_20211014_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='assesment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
