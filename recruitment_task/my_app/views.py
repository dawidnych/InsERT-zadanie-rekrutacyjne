from rest_framework import viewsets

from my_app.models import Category, Offers
from my_app.serializers import (
    CategoryDetailSerializer,
    CategorySerializer,
    OfferDetailSerializer,
    OffersSerializer,
)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return CategoryDetailSerializer
        return CategorySerializer


class OffersViewSet(viewsets.ModelViewSet):
    queryset = Offers.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return OfferDetailSerializer
        return OffersSerializer
