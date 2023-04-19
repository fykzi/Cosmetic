from django.db import models
from django.core.validators import MaxValueValidator


class Products(models.Model):
    brand = models.CharField("Бренд", max_length=50)
    title_of_product = models.CharField(
        "Название товара",
        max_length=100,
        blank=True,
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
        "Скидка, %", 
        default=0, 
        validators=[MaxValueValidator(100)]
    )

    class Meta:
        abstract = True


class Creams(Products):
    # Поля для фильтрации торваров
    cream_for = models.CharField("Крем для", max_length=20)
    type_of_derm = models.CharField("Тип кожи", max_length=50)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return f"(ID: {self.id}) brand: {self.brand} name: {self.title_of_product}"
