# Generated by Django 4.1.4 on 2022-12-24 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0005_alter_employee_job_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='company',
            field=models.CharField(choices=[('Softuni', 'Softuni'), ('Google', 'Google')], default='SoftUni', max_length=7),
            preserve_default=False,
        ),
    ]
