from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from import_export.formats import base_formats

from catalog.models import Creams, Perfumes, ModelFilters, Category
from catalog.resources import ProductResources


@admin.register(Creams, Perfumes)
class ProductsAdmin(ImportExportActionModelAdmin):
    list_display = (
        "id",
        "brand",
        "title_of_product",
        "short_description",
        "is_new",
        "price",
        "sale",
    )
    resources_class = ProductResources

    search_fields = ("id", "brand", "title_of_product", "is_new")

    list_filter = ("id", "price", "sale")

    def get_import_formats(self):
        return [base_formats.XLSX, base_formats.CSV]


@admin.register(ModelFilters)
class FilterAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["category"]
