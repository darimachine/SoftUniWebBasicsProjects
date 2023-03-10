# Generated by Django 4.1.4 on 2022-12-24 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0009_employee_deparment_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('employee_id', models.ManyToManyField(to='employees.employee')),
            ],
        ),
    ]
