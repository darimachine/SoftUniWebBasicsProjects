# Generated by Django 4.1.5 on 2023-01-08 22:02

import django.core.validators
from django.db import migrations, models
import main_app.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2, 'first name must be between 2 and 30'), main_app.validators.only_letters_validator])),
                ('last_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2, 'last name must be between 2 and 30'), main_app.validators.only_letters_validator])),
                ('picture', models.URLField()),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Do not show', 'Do not show')], max_length=11, null=True)),
            ],
        ),
    ]