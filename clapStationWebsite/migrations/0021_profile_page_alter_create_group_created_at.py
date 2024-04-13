# Generated by Django 4.2.3 on 2024-01-05 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clapStationWebsite', '0020_create_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('category', models.CharField(max_length=255)),
                ('subcategory', models.CharField(max_length=255)),
                ('budget', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='profileimage/')),
            ],
        ),
        migrations.AlterField(
            model_name='create_group',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]