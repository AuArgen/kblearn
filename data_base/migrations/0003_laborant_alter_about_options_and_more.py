# Generated by Django 4.0.6 on 2023-12-20 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_base', '0002_program'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laborant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Фамилия имя лаборанта:')),
                ('info', models.CharField(max_length=1000, verbose_name='Описание, может быть группа лаборантта и так далее...')),
            ],
            options={
                'verbose_name': '10 Кабинет',
                'verbose_name_plural': '10 Кабиненты',
            },
        ),
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name': '7 О нас', 'verbose_name_plural': '7 О нас'},
        ),
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name': '1 Категория', 'verbose_name_plural': '1 Категории'},
        ),
        migrations.AlterModelOptions(
            name='glav',
            options={'verbose_name': '4 Глава', 'verbose_name_plural': '4 Глава раздела'},
        ),
        migrations.AlterModelOptions(
            name='namecategories',
            options={'verbose_name': '2 Предмет ', 'verbose_name_plural': '2 Предметы категории'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': '6 Новость', 'verbose_name_plural': '6 Новости'},
        ),
        migrations.AlterModelOptions(
            name='program',
            options={'verbose_name': '8 Программа', 'verbose_name_plural': '8 Программы'},
        ),
        migrations.AlterModelOptions(
            name='raz',
            options={'verbose_name': '3 Раздел', 'verbose_name_plural': '3 Раздел предмета'},
        ),
        migrations.AlterModelOptions(
            name='theme',
            options={'verbose_name': '5 Тема', 'verbose_name_plural': '5 Тема главы'},
        ),
        migrations.CreateModel(
            name='Kabinet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Название кабинетта:')),
                ('info', models.CharField(max_length=1000, verbose_name='Описание...')),
                ('id_laborant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_base.laborant', verbose_name='Выберите лаборант:')),
            ],
            options={
                'verbose_name': '10 Кабинет',
                'verbose_name_plural': '10 Кабиненты',
            },
        ),
        migrations.CreateModel(
            name='Computers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название компьютер')),
                ('invb', models.CharField(max_length=15, verbose_name='ИНВ системный блок')),
                ('invm', models.CharField(max_length=15, verbose_name='ИНВ монитор')),
                ('hard', models.CharField(max_length=15, verbose_name='Размер жеский диск')),
                ('cart', models.CharField(max_length=15, verbose_name='Размер видео карта')),
                ('ram', models.CharField(max_length=15, verbose_name='Размер оперативный память')),
                ('id_kabinet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_base.kabinet', verbose_name='Из какого кабинента')),
            ],
            options={
                'verbose_name': '11 Компьютер',
                'verbose_name_plural': '11 Компьютеры',
            },
        ),
    ]