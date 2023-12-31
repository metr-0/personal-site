# Generated by Django 4.2.3 on 2023-09-08 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_block_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='block', related_query_name='blocks', to='main.page', verbose_name='page'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='row',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contacts', related_query_name='contact', to='main.row', verbose_name='row'),
        ),
        migrations.AlterField(
            model_name='row',
            name='block',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rows', related_query_name='row', to='main.block', verbose_name='block'),
        ),
    ]
