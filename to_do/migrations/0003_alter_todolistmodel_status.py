# Generated by Django 4.2.2 on 2023-06-19 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0002_alter_todolistmodel_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolistmodel',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
