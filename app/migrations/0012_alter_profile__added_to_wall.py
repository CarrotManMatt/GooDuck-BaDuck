# Generated by Django 4.1.2 on 2022-10-30 11:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_profile__added_to_wall_alter_profile_latitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='_added_to_wall',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 30, 10, 25, 16, 645785, tzinfo=datetime.timezone.utc), verbose_name='Last time added to wall'),
        ),
    ]
