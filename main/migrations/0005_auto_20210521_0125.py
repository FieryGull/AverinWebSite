# Generated by Django 2.2.5 on 2021-05-20 20:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210518_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homecontent',
            name='date',
            field=models.DateField(default=datetime.date(2021, 5, 21), verbose_name='Дата'),
        ),
    ]