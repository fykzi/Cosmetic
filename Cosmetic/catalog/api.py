from rest_framework.views import APIView
from rest_framework.response import Response
from openpyxl import open as open_excel

from catalog.serializers import CreamsSerializer
from catalog.models import Creams
from catalog.utils import get_filters_from_request, get_product_from_excel_row


class CreamsAPiView(APIView):

    def get(self, request):
        (
            filter_type_of_derm,
            filter_brand,
            filter_cream_for,
            price,
        ) = get_filters_from_request(request)

        creams = Creams.objects.filter(
            brand__in=filter_brand,
            type_of_derm__in=filter_type_of_derm,
            cream_for__in=filter_cream_for,
            price__range=price,
        )

        serializer = CreamsSerializer(creams, many=True)

        return Response({"data": serializer.data})

    def post(self, request):
        file = request.data['file'] if request.data['file'] else None
    
        if file:
            book = open_excel(file, read_only=True)  
            sheet = book.active
        else:
            return Response({'unsuccess': 'Файл не был передан'})

        for row in range(1, sheet.max_row + 1):
            (
                brand,
                title_of_product,
                short_description,
                description,
                price,
                is_new,
                sale,
                cream_for,
                type_of_derm,
            ) = get_product_from_excel_row(sheet[row])

            product_info = {
                "brand": brand,
                "title_of_product": title_of_product,
                "short_description": short_description,
                "description": description,
                "price": price,
                "is_new": is_new,
                "sale": sale,
                "cream_for": cream_for,
                "type_of_derm": type_of_derm,
            }
            serializer = CreamsSerializer(data=product_info)

            if serializer.is_valid(raise_exception=True):
                serializer.save()

        return Response(
            {"Success": "Товары успешно добавлены"}
        )
