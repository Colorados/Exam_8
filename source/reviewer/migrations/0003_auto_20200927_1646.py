# Generated by Django 2.2 on 2020-09-27 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewer', '0002_auto_20200926_0725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('other', 'Разное'), ('Food', 'Еда'), ('Toys', 'Игрушки'), ('Tools', 'Инструменты')], default='other', max_length=20, verbose_name='Категория товара'),
        ),
    ]
