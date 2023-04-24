from rest_framework import serializers

from catalog.models import Creams, Perfumes, ModelFilters


default_fields = [
    "id",
    "brand",
    "title_of_product",
    "short_description",
    "description",
    "price",
    "is_new",
    "sale",
]


class CreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creams
        fields = default_fields + ["cream_for", "type_of_derm"]


class PerfumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfumes
        fields = default_fields + ["perfume_volume", "perfume_aroma"]


class FilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelFilters

        fields = ["name", "name_of_filter_for_url", "fields"]
