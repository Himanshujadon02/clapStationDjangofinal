# Generated by Django 4.2.3 on 2024-01-09 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clapStationWebsite', '0045_delete_profilevideo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profilevideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('video', models.ImageField(upload_to='profilevideos/video')),
            ],
        ),
    ]