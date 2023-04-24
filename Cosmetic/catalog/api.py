from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

from catalog.serializers import CreamSerializer, PerfumeSerializer, FilterSerializer
from catalog.models import Creams, Perfumes, Category
from catalog.filters import CreamFilter, PerfumeFilter


class CreamsAPi(ListAPIView):
    queryset = Creams.objects.all()
    serializer_class = CreamSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CreamFilter


class PerfumesAPi(ListAPIView):
    queryset = Perfumes.objects.all()
    serializer_class = PerfumeSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PerfumeFilter


class CategoryApi(ListAPIView):
    serializer_class = FilterSerializer

    def get_queryset(self):
        category = self.kwargs["category"].lower()
        catalog_models = ["cream", "perfume"]

        if category in catalog_models:
            filters = Category.objects.get(category__icontains=category).filters.all()
            return filters


        
        # if category in catalog_models:
        #     return ModelFilters.objects.filter(name__in=filters)

    # def get(self, request):
    #     (
    #         filter_type_of_derm,
    #         filter_brand,
    #         filter_cream_for,
    #         price,
    #     ) = get_filters_from_request(request)

    #     creams = Creams.objects.filter(
    #         brand__in=filter_brand,
    #         type_of_derm__in=filter_type_of_derm,
    #         cream_for__in=filter_cream_for,
    #         price__range=price,
    #     )

    #     serializer = CreamsSerializer(creams, many=True)

    #     return Response({"data": serializer.data})

    # def post(self, request):
    #     file = request.data['file'] if request.data['file'] else None

    #     if file:
    #         book = open_excel(file, read_only=True)
    #         sheet = book.active
    #     else:
    #         return Response({'unsuccess': 'Файл не был передан'})

    #     for row in range(1, sheet.max_row + 1):
    #         (
    #             brand,
    #             title_of_product,
    #             short_description,
    #             description,
    #             price,
    #             is_new,
    #             sale,
    #             cream_for,
    #             type_of_derm,
    #         ) = get_product_from_excel_row(sheet[row])

    #         product_info = {
    #             "brand": brand,
    #             "title_of_product": title_of_product,
    #             "short_description": short_description,
    #             "description": description,
    #             "price": price,
    #             "is_new": is_new,
    #             "sale": sale,
    #             "cream_for": cream_for,
    #             "type_of_derm": type_of_derm,
    #         }
    #         serializer = CreamsSerializer(data=product_info)

    #         if serializer.is_valid(raise_exception=True):
    #             serializer.save()

    #     return Response(
    #         {"Success": "Товары успешно добавлены"}
    #     )
