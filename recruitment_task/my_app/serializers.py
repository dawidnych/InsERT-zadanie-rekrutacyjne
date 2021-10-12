from rest_framework import serializers

from my_app.models import Category, Offers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CategoryDetailSerializer(CategorySerializer):
    class Meta:
        model = Category
        fields = ("name",)


class OffersSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(), slug_field="id"
    )

    class Meta:
        model = Offers
        fields = "__all__"


class OfferDetailSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.name")

    class Meta:
        model = Offers
        fields = (
            "title",
            "description",
            "price",
            "created_at",
            "category",
        )
