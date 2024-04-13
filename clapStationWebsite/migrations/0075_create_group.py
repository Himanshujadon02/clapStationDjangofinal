# Generated by Django 4.2.3 on 2024-02-10 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clapStationWebsite', '0074_delete_create_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Create_group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupname', models.CharField(max_length=20)),
                ('singername', models.CharField(max_length=20)),
                ('singerprofession', models.CharField(max_length=20)),
                ('singeraddress', models.CharField(max_length=20)),
                ('singerimage', models.ImageField(blank=True, default='no image found', null=True, upload_to='createsingerimage/image')),
                ('singerinstagramid', models.CharField(max_length=50)),
                ('singerlinkedinid', models.CharField(max_length=50)),
                ('musicianname', models.CharField(max_length=20)),
                ('musicianprofession', models.CharField(max_length=20)),
                ('musicianaddress', models.CharField(max_length=20)),
                ('musicianimage', models.ImageField(blank=True, default='no image found', null=True, upload_to='musicianimage/image')),
                ('musicianinstagramid', models.CharField(max_length=50)),
                ('musicianlinkedinid', models.CharField(max_length=50)),
                ('vocalistname', models.CharField(max_length=20)),
                ('vocalistprofession', models.CharField(max_length=20)),
                ('vocalistaddress', models.CharField(max_length=20)),
                ('vocalistimage', models.ImageField(blank=True, default='no image found', null=True, upload_to='vocalistimage/image')),
                ('vocalistinstagramid', models.CharField(max_length=50)),
                ('vocalistlinkedinid', models.CharField(max_length=50)),
                ('guitaristname', models.CharField(max_length=20)),
                ('guitaristprofession', models.CharField(max_length=20)),
                ('guitaristaddress', models.CharField(max_length=20)),
                ('guitaristimage', models.ImageField(blank=True, default='no image found', null=True, upload_to='guitaristimage/image')),
                ('guitaristinstagramid', models.CharField(max_length=50)),
                ('guitaristlinkedinid', models.CharField(max_length=50)),
                ('groupdescription', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
