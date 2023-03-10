# Generated by Django 4.1.5 on 2023-01-29 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_rename_descripion_expense_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expense',
            options={'ordering': ('title', 'price')},
        ),
        migrations.AlterField(
            model_name='expense',
            name='image',
            field=models.URLField(verbose_name='Link to Image'),
        ),
    ]
