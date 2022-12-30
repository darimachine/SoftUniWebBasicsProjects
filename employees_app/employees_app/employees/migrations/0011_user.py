# Generated by Django 4.1.4 on 2022-12-24 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0010_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='employees.employee')),
            ],
        ),
    ]