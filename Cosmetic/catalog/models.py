from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class ModelFilters(models.Model):
    name = models.CharField("Имя фильтра", max_length=20)
    name_of_filter_for_url = models.CharField(
        "Имя фильтра для запроса", max_length=20, default=None
    )
    fields = models.JSONField(
        "Поля фильтра (имя поля: имя поля для url)"
    )  # Например: Сухой: dry, comb: Комбинированной

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Фильтр"
        verbose_name_plural = "Фильтры"


class Category(models.Model):
    category = models.CharField("Категория", max_length=15)
    filters = models.ManyToManyField(ModelFilters)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Products(models.Model):
    brand = models.CharField("Бренд", max_length=50)
    title_of_product = models.CharField(
        "Название товара",
        max_length=100,
    )
    short_description = models.CharField(
        "Краткое описание",
        max_length=25,
        blank=True,
    )
    description = models.TextField("Описание", blank=True)
    price = models.PositiveIntegerField("Цена")
    is_new = models.BooleanField("Новинка", default=False)
    sale = models.PositiveIntegerField(
        "Скидка, %", default=0, validators=[MaxValueValidator(100)]
    )

    def __str__(self):
        return f"(ID: {self.id}) brand: {self.brand} name: {self.title_of_product}"

    class Meta:
        abstract = True


class Creams(Products):
    cream_for = models.CharField("Крем для", max_length=20)
    type_of_derm = models.CharField("Тип кожи", max_length=50)

    class Meta:
        verbose_name = "Крем"
        verbose_name_plural = "Кремы"


class Perfumes(Products):
    perfume_aroma = models.CharField("Аромат", max_length=25)
    perfume_volume = models.PositiveIntegerField(
        "Объём",
        validators=[MinValueValidator],
    )

    class Meta:
        verbose_name = "Парфюм"
        verbose_name_plural = "Парфюм"
