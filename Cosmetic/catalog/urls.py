from django.urls import path

from catalog.api import CreamsAPi, PerfumesAPi, CategoryApi


urlpatterns = [
    path("products/Creams/", CreamsAPi.as_view()),
    path("products/Perfumes/", PerfumesAPi.as_view()),
    path("<category>/", CategoryApi.as_view()),
]
