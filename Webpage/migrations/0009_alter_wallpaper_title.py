# Generated by Django 4.1.4 on 2023-03-21 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webpage', '0008_wallpaper_my_choice_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallpaper',
            name='Title',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]