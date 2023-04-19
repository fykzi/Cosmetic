from rest_framework import serializers

from catalog.models import Creams


class CreamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creams
        fields = [
            "id",
            "brand",
            "title_of_product",
            "short_description",
            "description",
            "price",
            'is_new',
            'sale',
            'cream_for',
            'type_of_derm',
        ]
