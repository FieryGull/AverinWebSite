# Generated by Django 2.2.5 on 2021-05-25 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20210525_0523'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectsblock',
            name='full_text_en',
            field=models.TextField(null=True, verbose_name='Контент блока'),
        ),
        migrations.AddField(
            model_name='projectsblock',
            name='full_text_ru',
            field=models.TextField(null=True, verbose_name='Контент блока'),
        ),
        migrations.AddField(
            model_name='projectsblock',
            name='title_en',
            field=models.CharField(max_length=50, null=True, verbose_name='Подзаголовок блока информации'),
        ),
        migrations.AddField(
            model_name='projectsblock',
            name='title_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='Подзаголовок блока информации'),
        ),
        migrations.AddField(
            model_name='projectscontent',
            name='main_title_en',
            field=models.CharField(default='Заголовок по-умолчанию', max_length=50, null=True, verbose_name='Заголовок страницы'),
        ),
        migrations.AddField(
            model_name='projectscontent',
            name='main_title_ru',
            field=models.CharField(default='Заголовок по-умолчанию', max_length=50, null=True, verbose_name='Заголовок страницы'),
        ),
    ]
