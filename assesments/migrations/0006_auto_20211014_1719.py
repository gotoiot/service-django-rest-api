# Generated by Django 3.2.8 on 2021-10-14 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assesments', '0005_auto_20211007_1814'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='assesment',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='instance',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='option',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='taker',
            options={'ordering': ['-id']},
        ),
        migrations.RemoveField(
            model_name='assesment',
            name='created',
        ),
        migrations.RemoveField(
            model_name='instance',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='instance',
            name='start_date',
        ),
    ]
