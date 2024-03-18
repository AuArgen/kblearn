# Generated by Django 4.0.6 on 2023-04-13 00:46

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('tel', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None)),
                ('telInfo', models.TextField(default=0)),
                ('password', models.TextField(null=True)),
            ],
        ),
    ]
