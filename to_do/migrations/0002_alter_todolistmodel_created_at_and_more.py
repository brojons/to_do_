# Generated by Django 4.2.2 on 2023-06-19 10:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolistmodel',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='todolistmodel',
            name='update_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
