# Generated by Django 4.2.3 on 2023-12-26 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clapStationWebsite', '0012_delete_event_detail_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event_detail_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventname', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('budget', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='event_images/')),
            ],
        ),
    ]