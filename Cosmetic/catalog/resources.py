from import_export import resources

from catalog.models import Creams, Perfumes


class ProductResources(resources.ModelResource):
    class Meta:
        models = [Creams, Perfumes]
