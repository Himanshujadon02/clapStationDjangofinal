# Generated by Django 4.2.3 on 2024-02-13 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clapStationWebsite', '0091_eventimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventimage',
            name='event',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='EventImage',
        ),
    ]
