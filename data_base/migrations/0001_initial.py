# Generated by Django 4.0.6 on 2023-04-13 00:46

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media/photo/%Y/%m/%d', verbose_name='изображение работника')),
                ('fio', models.CharField(max_length=255, verbose_name='Фамилия, Имя, Отечества')),
                ('slug', models.SlugField(help_text='Поля автоматический заполняется!')),
                ('special', models.CharField(max_length=255, verbose_name='специалисть')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, unique=True, verbose_name='Телефон номер')),
                ('rezume', models.FileField(blank=True, null=True, upload_to='files/%Y/%m/%d', verbose_name='резюме необезательно')),
            ],
            options={
                'verbose_name': 'О нас',
                'verbose_name_plural': 'О нас',
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='категория')),
                ('slug', models.SlugField(blank=True, help_text='Поля автоматический заполняется!', null=True)),
                ('image', models.ImageField(upload_to='media/photo/%Y/%m/%d', verbose_name='изображение категории')),
                ('count', models.IntegerField(verbose_name='номер категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Glav',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='глава раздела')),
                ('slug', models.SlugField(blank=True, help_text='Поля автоматический заполняется!', null=True)),
            ],
            options={
                'verbose_name': 'Глава',
                'verbose_name_plural': 'Глава раздела',
            },
        ),
        migrations.CreateModel(
            name='NameCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='название предмета')),
                ('slug', models.SlugField(blank=True, help_text='Поля автоматический заполняется!', null=True)),
                ('id_cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_base.categories', verbose_name='Из какого категории')),
            ],
            options={
                'verbose_name': 'Предмет ',
                'verbose_name_plural': 'Предметы категории',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название новости')),
                ('text', ckeditor.fields.RichTextField(verbose_name='Текст:')),
                ('img', models.ImageField(blank=True, upload_to='media/photo/%Y/%m/%d', verbose_name='изображение новость')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name="дата новость 'автоматически заполняется'")),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.TextField(verbose_name='Тема:')),
                ('full_text', ckeditor.fields.RichTextField(verbose_name='Тексе:')),
                ('slug', models.SlugField(blank=True, help_text='Поля автоматический заполняется!', null=True)),
                ('id_glav', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_base.glav', verbose_name='Из какого глава')),
            ],
            options={
                'verbose_name': 'Тема',
                'verbose_name_plural': 'Тема главы',
            },
        ),
        migrations.CreateModel(
            name='Raz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='раздел предмета')),
                ('slug', models.SlugField(blank=True, help_text='Поля автоматический заполняется!', null=True)),
                ('categori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_base.namecategories', verbose_name='Из какого предмета')),
            ],
            options={
                'verbose_name': 'Раздел',
                'verbose_name_plural': 'Раздел предмета',
            },
        ),
        migrations.AddField(
            model_name='glav',
            name='razdel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_base.raz', verbose_name='Из какого раздела'),
        ),
    ]
