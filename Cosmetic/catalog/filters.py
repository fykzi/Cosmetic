from django_filters import FilterSet
import django_filters as filters

from catalog.models import Creams, Perfumes


class ProductFilter(FilterSet):
    brand = filters.BaseInFilter()
    price = filters.RangeFilter()


class CreamFilter(ProductFilter):
    cream_for = filters.BaseInFilter()
    type_of_derm = filters.BaseInFilter()

    class Meta:
        model = Creams
        fields = [
            "brand",
            "price",
            "cream_for",
            "type_of_derm",
        ]


class PerfumeFilter(ProductFilter):
    perfume_aroma = filters.BaseInFilter()
    perfume_volume = filters.RangeFilter()

    class Meta:
        model = Perfumes
        fields = [
            "brand",
            "price",
            "perfume_aroma",
            "perfume_volume",
        ]
