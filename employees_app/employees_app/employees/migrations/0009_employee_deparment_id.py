# Generated by Django 4.1.4 on 2022-12-24 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0008_department_alter_employee_egn'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='deparment_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='employees.department'),
            preserve_default=False,
        ),
    ]
