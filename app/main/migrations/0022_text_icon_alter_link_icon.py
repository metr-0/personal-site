# Generated by Django 4.2.3 on 2023-09-08 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_alter_link_options_alter_text_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='icon'),
        ),
        migrations.AlterField(
            model_name='link',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='icon'),
        ),
    ]
