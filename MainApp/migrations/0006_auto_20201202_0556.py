# Generated by Django 3.1.3 on 2020-12-02 05:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0005_auto_20201201_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 2, 5, 56, 27, 899302)),
        ),
    ]