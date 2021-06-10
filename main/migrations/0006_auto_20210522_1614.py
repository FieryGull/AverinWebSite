# Generated by Django 2.2.5 on 2021-05-22 11:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210521_0125'),
    ]

    operations = [
        migrations.CreateModel(
            name='BiographyContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_title', models.CharField(default='Заголовок по-умолчанию', max_length=50, verbose_name='Заголовок страницы')),
            ],
            options={
                'verbose_name': 'Контент биографической справки',
                'verbose_name_plural': 'Контент биографической справки',
            },
        ),
        migrations.AlterField(
            model_name='homecontent',
            name='date',
            field=models.DateField(default=datetime.date(2021, 5, 22), verbose_name='Дата'),
        ),
        migrations.CreateModel(
            name='BiographyBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название блока')),
                ('full_text', models.TextField(verbose_name='Контент')),
                ('date', models.DateField(default=datetime.date(2021, 5, 22), verbose_name='Дата')),
                ('BiographyContent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.BiographyContent')),
            ],
        ),
    ]