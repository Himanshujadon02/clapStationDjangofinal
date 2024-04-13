# Generated by Django 4.2.3 on 2024-01-07 13:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clapStationWebsite', '0028_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=100)),
                ('subcategory', models.CharField(max_length=100)),
                ('budget', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(default='static/images/profile-1.png', upload_to='profile/image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]