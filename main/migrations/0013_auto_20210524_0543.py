# Generated by Django 2.2.5 on 2021-05-24 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20210524_0529'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicationscontent',
            name='title_en',
            field=models.CharField(max_length=50, null=True, verbose_name='Подзаголовок блока информации'),
        ),
        migrations.AddField(
            model_name='publicationscontent',
            name='title_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='Подзаголовок блока информации'),
        ),
    ]
