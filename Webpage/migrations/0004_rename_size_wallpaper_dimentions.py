# Generated by Django 4.1.4 on 2023-03-18 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Webpage', '0003_wallpaper_size'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wallpaper',
            old_name='Size',
            new_name='Dimentions',
        ),
    ]
