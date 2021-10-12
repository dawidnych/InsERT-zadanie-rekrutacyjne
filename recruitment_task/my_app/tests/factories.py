import factory

from my_app.models import Category, Offers


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker("pystr")
    ordering = factory.Sequence(lambda n: n)


class OffersFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Offers

    title = factory.Faker("pystr")
    description = factory.Faker("pystr")
    price = 9.99
    created_at = factory.Faker("date_between", start_date="-7d", end_date="-1d")
    category = factory.SubFactory(CategoryFactory)
