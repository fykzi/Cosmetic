from django.contrib import admin

from catalog.models import Creams


@admin.register(Creams)
class ProductsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "brand",
        "title_of_product",
        "short_description",
        'is_new',
        "price",
        'sale',
    )

    search_fields = ("id", "brand", "title_of_product", 'is_new')

    list_filter = ("id", "price", 'sale')
