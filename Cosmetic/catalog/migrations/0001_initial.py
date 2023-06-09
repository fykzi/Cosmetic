# Generated by Django 4.2 on 2023-04-24 09:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Creams",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("brand", models.CharField(max_length=50, verbose_name="Бренд")),
                (
                    "title_of_product",
                    models.CharField(max_length=100, verbose_name="Название товара"),
                ),
                (
                    "short_description",
                    models.CharField(
                        blank=True, max_length=25, verbose_name="Краткое описание"
                    ),
                ),
                ("description", models.TextField(blank=True, verbose_name="Описание")),
                ("price", models.PositiveIntegerField(verbose_name="Цена")),
                ("is_new", models.BooleanField(default=False, verbose_name="Новинка")),
                (
                    "sale",
                    models.PositiveIntegerField(
                        default=0,
                        validators=[django.core.validators.MaxValueValidator(100)],
                        verbose_name="Скидка, %",
                    ),
                ),
                ("cream_for", models.CharField(max_length=20, verbose_name="Крем для")),
                (
                    "type_of_derm",
                    models.CharField(max_length=50, verbose_name="Тип кожи"),
                ),
            ],
            options={
                "verbose_name": "Крем",
                "verbose_name_plural": "Кремы",
            },
        ),
        migrations.CreateModel(
            name="ModelFilters",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20, verbose_name="Имя фильтра")),
                (
                    "name_of_filter_for_url",
                    models.CharField(
                        default=None,
                        max_length=20,
                        verbose_name="Имя фильтра для запроса",
                    ),
                ),
                (
                    "fields",
                    models.JSONField(
                        verbose_name="Поля фильтра (имя поля: имя поля для url)"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Perfumes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("brand", models.CharField(max_length=50, verbose_name="Бренд")),
                (
                    "title_of_product",
                    models.CharField(max_length=100, verbose_name="Название товара"),
                ),
                (
                    "short_description",
                    models.CharField(
                        blank=True, max_length=25, verbose_name="Краткое описание"
                    ),
                ),
                ("description", models.TextField(blank=True, verbose_name="Описание")),
                ("price", models.PositiveIntegerField(verbose_name="Цена")),
                ("is_new", models.BooleanField(default=False, verbose_name="Новинка")),
                (
                    "sale",
                    models.PositiveIntegerField(
                        default=0,
                        validators=[django.core.validators.MaxValueValidator(100)],
                        verbose_name="Скидка, %",
                    ),
                ),
                (
                    "perfume_aroma",
                    models.CharField(max_length=25, verbose_name="Аромат"),
                ),
                (
                    "perfume_volume",
                    models.PositiveIntegerField(
                        validators=[django.core.validators.MinValueValidator],
                        verbose_name="Объём",
                    ),
                ),
            ],
            options={
                "verbose_name": "Парфюм",
                "verbose_name_plural": "Парфюм",
            },
        ),
    ]
