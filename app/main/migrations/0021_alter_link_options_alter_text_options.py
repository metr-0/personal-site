# Generated by Django 4.2.3 on 2023-09-08 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_alter_link_row_text'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'verbose_name': 'link', 'verbose_name_plural': 'links'},
        ),
        migrations.AlterModelOptions(
            name='text',
            options={'verbose_name': 'text', 'verbose_name_plural': 'texts'},
        ),
    ]
