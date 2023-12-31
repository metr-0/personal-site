# Generated by Django 4.2.3 on 2023-08-16 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_contact_foreground_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255, verbose_name='описание')),
                ('order_id', models.IntegerField(verbose_name='порядковый номер')),
            ],
            options={
                'verbose_name': 'блок',
                'verbose_name_plural': 'блоки',
                'ordering': ['order_id'],
            },
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['order_id'], 'verbose_name': 'контакт', 'verbose_name_plural': 'контакты'},
        ),
        migrations.RemoveField(
            model_name='contact',
            name='column',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='is_visible',
        ),
        migrations.AddField(
            model_name='contact',
            name='order_id',
            field=models.IntegerField(default=1, verbose_name='Порядковый номер'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Row',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(verbose_name='порядковый номер')),
                ('block', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rows', related_query_name='row', to='main.block')),
            ],
            options={
                'verbose_name': 'ряд',
                'verbose_name_plural': 'ряды',
                'ordering': ['order_id'],
            },
        ),
        migrations.AlterField(
            model_name='contact',
            name='row',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contacts', related_query_name='contact', to='main.row'),
        ),
    ]
