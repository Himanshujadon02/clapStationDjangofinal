# Generated by Django 4.2.3 on 2024-01-19 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clapStationWebsite', '0066_posts_like'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profilephoto',
        ),
        migrations.DeleteModel(
            name='Profilevideo',
        ),
    ]
