# Generated by Django 4.2.3 on 2023-09-08 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_page_options_page_is_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pages', related_query_name='page', to='main.page', verbose_name='page'),
        ),
    ]
