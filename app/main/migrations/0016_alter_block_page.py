# Generated by Django 4.2.3 on 2023-09-08 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_block_page_alter_contact_row_alter_row_block'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blocks', related_query_name='block', to='main.page', verbose_name='page'),
        ),
    ]
