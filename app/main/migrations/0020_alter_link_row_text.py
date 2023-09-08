# Generated by Django 4.2.3 on 2023-09-08 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20230908_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='row',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)ss', related_query_name='%(class)s', to='main.row', verbose_name='row'),
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('order_id', models.IntegerField(verbose_name='order_id')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('row', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)ss', related_query_name='%(class)s', to='main.row', verbose_name='row')),
            ],
            options={
                'verbose_name': 'item',
                'verbose_name_plural': 'items',
                'ordering': ['order_id'],
                'abstract': False,
            },
        ),
    ]