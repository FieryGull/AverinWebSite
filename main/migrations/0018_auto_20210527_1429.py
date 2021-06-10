# Generated by Django 2.2.5 on 2021-05-27 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20210525_1001'),
    ]

    operations = [
        migrations.CreateModel(
            name='AchievementBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_title', models.CharField(max_length=50, verbose_name='Подзаголовок блока информации')),
                ('block_title_ru', models.CharField(max_length=50, null=True, verbose_name='Подзаголовок блока информации')),
                ('block_title_en', models.CharField(max_length=50, null=True, verbose_name='Подзаголовок блока информации')),
                ('block_text', models.TextField(verbose_name='Контент блока')),
                ('block_text_ru', models.TextField(null=True, verbose_name='Контент блока')),
                ('block_text_en', models.TextField(null=True, verbose_name='Контент блока')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Контент страницы достижений',
                'verbose_name_plural': 'Контент страницы достижений',
            },
        ),
        migrations.CreateModel(
            name='ConferenceBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_title', models.CharField(max_length=50, verbose_name='Подзаголовок блока информации')),
                ('block_title_ru', models.CharField(max_length=50, null=True, verbose_name='Подзаголовок блока информации')),
                ('block_title_en', models.CharField(max_length=50, null=True, verbose_name='Подзаголовок блока информации')),
                ('block_text', models.TextField(verbose_name='Контент блока')),
                ('block_text_ru', models.TextField(null=True, verbose_name='Контент блока')),
                ('block_text_en', models.TextField(null=True, verbose_name='Контент блока')),
                ('link_image', models.CharField(default='/', max_length=200, verbose_name='Ссылка на изображение')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Контент страницы конференций',
                'verbose_name_plural': 'Контент страницы конференций',
            },
        ),
        migrations.CreateModel(
            name='CourseBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_title', models.CharField(max_length=50, verbose_name='Подзаголовок блока информации')),
                ('block_title_ru', models.CharField(max_length=50, null=True, verbose_name='Подзаголовок блока информации')),
                ('block_title_en', models.CharField(max_length=50, null=True, verbose_name='Подзаголовок блока информации')),
                ('block_text', models.TextField(verbose_name='Описание')),
                ('block_text_ru', models.TextField(null=True, verbose_name='Описание')),
                ('block_text_en', models.TextField(null=True, verbose_name='Описание')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Контент страницы курсов',
                'verbose_name_plural': 'Контент страницы курсов',
            },
        ),
        migrations.CreateModel(
            name='CourseVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_name', models.CharField(max_length=50, verbose_name='Наименование видео')),
                ('video_name_ru', models.CharField(max_length=50, null=True, verbose_name='Наименование видео')),
                ('video_name_en', models.CharField(max_length=50, null=True, verbose_name='Наименование видео')),
                ('link', models.CharField(max_length=100, verbose_name='Ссылка на видео')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата')),
                ('CourseBlock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.CourseBlock')),
            ],
            options={
                'verbose_name': 'Видео',
                'verbose_name_plural': 'Видео',
            },
        ),
        migrations.CreateModel(
            name='HomeBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_title', models.CharField(max_length=50, verbose_name='Подзаголовок блока информации')),
                ('block_title_ru', models.CharField(max_length=50, null=True, verbose_name='Подзаголовок блока информации')),
                ('block_title_en', models.CharField(max_length=50, null=True, verbose_name='Подзаголовок блока информации')),
                ('block_text', models.TextField(verbose_name='Контент блока')),
                ('block_text_ru', models.TextField(null=True, verbose_name='Контент блока')),
                ('block_text_en', models.TextField(null=True, verbose_name='Контент блока')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Контент главной страницы',
                'verbose_name_plural': 'Контент главной страницы',
            },
        ),
        migrations.CreateModel(
            name='NavContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo_text', models.CharField(max_length=50, verbose_name='Текст логотипа')),
                ('logo_text_ru', models.CharField(max_length=50, null=True, verbose_name='Текст логотипа')),
                ('logo_text_en', models.CharField(max_length=50, null=True, verbose_name='Текст логотипа')),
                ('link_logo_image', models.CharField(max_length=50, verbose_name='Ссылка на фотографию')),
                ('email', models.EmailField(max_length=50, verbose_name='Почта')),
                ('link_yt', models.CharField(max_length=100, verbose_name='Ссылка на YouTube')),
                ('link_inst', models.CharField(max_length=100, verbose_name='Ссылка на Instagram')),
                ('link_vk', models.CharField(max_length=100, verbose_name='Ссылка на VK')),
                ('link_fb', models.CharField(max_length=100, verbose_name='Ссылка на Ссылка на Facebook')),
                ('link_rg', models.CharField(max_length=100, verbose_name='Ссылка на ResearchGate')),
                ('link_orcid', models.CharField(max_length=100, verbose_name='Ссылка на ORCID')),
                ('link_gs', models.CharField(max_length=100, verbose_name='Ссылка на GoogleScholar')),
                ('link_scopus', models.CharField(max_length=100, verbose_name='Ссылка на Scopus')),
                ('link_publons', models.CharField(max_length=100, verbose_name='Ссылка на Publons')),
            ],
            options={
                'verbose_name': 'Контент навигационного меню и ссылок с главной страницы',
                'verbose_name_plural': 'Контент навигационного меню и ссылок с главной страницы',
            },
        ),
        migrations.CreateModel(
            name='ProjectBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_title', models.CharField(max_length=50, verbose_name='Подзаголовок блока информации')),
                ('block_title_ru', models.CharField(max_length=50, null=True, verbose_name='Подзаголовок блока информации')),
                ('block_title_en', models.CharField(max_length=50, null=True, verbose_name='Подзаголовок блока информации')),
                ('block_text', models.TextField(verbose_name='Контент блока')),
                ('block_text_ru', models.TextField(null=True, verbose_name='Контент блока')),
                ('block_text_en', models.TextField(null=True, verbose_name='Контент блока')),
                ('link_image', models.CharField(default='/', max_length=200, verbose_name='Ссылка на изображение')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Контент страницы проектов',
                'verbose_name_plural': 'Контент страницы проектов',
            },
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Наименование публикации')),
                ('name_ru', models.TextField(null=True, verbose_name='Наименование публикации')),
                ('name_en', models.TextField(null=True, verbose_name='Наименование публикации')),
                ('authors_publications', models.TextField(verbose_name='Авторы')),
                ('authors_publications_ru', models.TextField(null=True, verbose_name='Авторы')),
                ('authors_publications_en', models.TextField(null=True, verbose_name='Авторы')),
                ('other_text', models.TextField(verbose_name='Другая информация')),
                ('other_text_ru', models.TextField(null=True, verbose_name='Другая информация')),
                ('other_text_en', models.TextField(null=True, verbose_name='Другая информация')),
                ('link', models.CharField(max_length=50, verbose_name='Ссылка на публикацию')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Публикация',
                'verbose_name_plural': 'Публикации',
            },
        ),
        migrations.CreateModel(
            name='PublicationBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_title', models.CharField(max_length=50, verbose_name='Подзаголовок блока информации')),
                ('block_title_ru', models.CharField(max_length=50, null=True, verbose_name='Подзаголовок блока информации')),
                ('block_title_en', models.CharField(max_length=50, null=True, verbose_name='Подзаголовок блока информации')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Контент страницы публикаций',
                'verbose_name_plural': 'Контент страницы публикаций',
            },
        ),
        migrations.RemoveField(
            model_name='conferencesblock',
            name='ConferencesContent',
        ),
        migrations.DeleteModel(
            name='HomeContent',
        ),
        migrations.RemoveField(
            model_name='projectsblock',
            name='ProjectsContent',
        ),
        migrations.RemoveField(
            model_name='publicationsblock',
            name='PublicationsBlock',
        ),
        migrations.RemoveField(
            model_name='scienceprogressblock',
            name='ScienceProgressContent',
        ),
        migrations.AlterModelOptions(
            name='biographyblock',
            options={'verbose_name': 'Контент биографической справки', 'verbose_name_plural': 'Контент биографической справки'},
        ),
        migrations.RenameField(
            model_name='biographyblock',
            old_name='full_text',
            new_name='block_text',
        ),
        migrations.RenameField(
            model_name='biographyblock',
            old_name='full_text_en',
            new_name='block_text_en',
        ),
        migrations.RenameField(
            model_name='biographyblock',
            old_name='full_text_ru',
            new_name='block_text_ru',
        ),
        migrations.RenameField(
            model_name='biographyblock',
            old_name='title',
            new_name='block_title',
        ),
        migrations.RenameField(
            model_name='biographyblock',
            old_name='title_en',
            new_name='block_title_en',
        ),
        migrations.RenameField(
            model_name='biographyblock',
            old_name='title_ru',
            new_name='block_title_ru',
        ),
        migrations.RemoveField(
            model_name='biographyblock',
            name='BiographyContent',
        ),
        migrations.AlterField(
            model_name='biographyblock',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата'),
        ),
        migrations.DeleteModel(
            name='BiographyContent',
        ),
        migrations.DeleteModel(
            name='ConferencesBlock',
        ),
        migrations.DeleteModel(
            name='ConferencesContent',
        ),
        migrations.DeleteModel(
            name='ProjectsBlock',
        ),
        migrations.DeleteModel(
            name='ProjectsContent',
        ),
        migrations.DeleteModel(
            name='PublicationsBlock',
        ),
        migrations.DeleteModel(
            name='PublicationsContent',
        ),
        migrations.DeleteModel(
            name='ScienceProgressBlock',
        ),
        migrations.DeleteModel(
            name='ScienceProgressContent',
        ),
        migrations.AddField(
            model_name='publication',
            name='PublicationsBlock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.PublicationBlock'),
        ),
    ]
