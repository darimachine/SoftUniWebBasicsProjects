# Generated by Django 4.1.4 on 2023-01-17 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0014_employee_image_alter_employee_egn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profiles'),
        ),
    ]
