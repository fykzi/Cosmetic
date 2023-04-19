# Generated by Django 4.2 on 2023-04-14 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Creams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50, verbose_name='Бренд')),
                ('title_of_product', models.CharField(max_length=50, verbose_name='Название товара')),
                ('type_of_derm', models.CharField(max_length=50, verbose_name='Тип продукта')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('cream_for', models.CharField(max_length=20, verbose_name='Крем для')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]