# Generated by Django 4.2.3 on 2023-09-08 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_contact_options_alter_contact_row'),
    ]

    operations = [
        migrations.RenameModel('Contact', 'Link')
    ]