# Generated by Django 4.2.4 on 2023-09-10 06:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid_app', '0010_remove_contact_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='time',
            field=models.TimeField(default=datetime.time(12, 2, 15, 393607)),
        ),
    ]