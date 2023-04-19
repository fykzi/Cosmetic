def get_filters_from_request(request):
    type_of_derm = request.query_params.get("d")
    brand = request.query_params.get("b")
    product_for_who = request.query_params.get("w")
    price = request.query_params.get("p")

    filters_for_product = [type_of_derm, brand, product_for_who]

    for index, filter_for_field in enumerate(filters_for_product):
        try:
            filters = filter_for_field.split(",")
            filters_for_product[index] = filters
        except (AttributeError, TypeError):
            filters_for_product[index] = []

    if price:
        price = map(int, price.split(","))
    else:
        price = [0, 10000]

    filters_for_product.append(price)

    return filters_for_product


def get_product_from_excel_row(excel_row):
    product_field = list()

    for cell in excel_row:
        product_field.append(cell.value)
    
    return product_field