# Generated by Django 4.1.4 on 2023-01-17 17:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0013_rename_deparment_id_employee_deparment'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='employee',
            name='egn',
            field=models.CharField(default='', max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(10)], verbose_name='EGN'),
        ),
    ]
