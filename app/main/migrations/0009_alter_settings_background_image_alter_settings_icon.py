# Generated by Django 4.2.3 on 2023-08-20 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_settings_logo_settings_icon_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='background_image',
            field=models.ImageField(upload_to='', verbose_name='background-image'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='icon',
            field=models.ImageField(upload_to='', verbose_name='icon'),
        ),
    ]