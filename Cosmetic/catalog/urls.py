from django.urls import path

from catalog.api import CreamsAPiView


urlpatterns = [
    path("products/", CreamsAPiView.as_view()),
]
