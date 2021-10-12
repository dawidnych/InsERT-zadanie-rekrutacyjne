import pytest

from my_app.models import Offers
from my_app.tests.factories import CategoryFactory, OffersFactory


@pytest.mark.django_db
class TestOffers:
    def test_create_offer(self, client):
        category = CategoryFactory()
        assert Offers.objects.count() == 0

        response = client.post(
            "/offers/",
            {
                "title": "Offer1",
                "description": "Offer description",
                "price": 9.99,
                "category": category.id,
            },
        )

        assert response.status_code == 201
        assert Offers.objects.count() == 1
        assert response.json()["id"] == 1
        assert response.json()["title"] == "Offer1"
        assert response.json()["description"] == "Offer description"
        assert response.json()["price"] == 9.99
        assert response.json()["category"] == category.id

    def test_list_offer(self, client):
        OffersFactory.create_batch(5)

        response = client.get("/offers/")

        assert response.status_code == 200
        assert len(response.json()) == 5

    def test_detail_offer(self, client):
        offer = OffersFactory()

        response = client.get(f"/offers/{offer.id}/")

        assert response.status_code == 200
        assert response.json()["title"] == offer.title
        assert response.json()["description"] == offer.description
        assert response.json()["price"] == offer.price
        assert response.json()["category"] == offer.category.name

    def test_update_offer(self, client):
        offer = OffersFactory()
        category = CategoryFactory()

        response_put = client.put(
            f"/offers/{offer.id}/",
            {
                "title": "Offer1",
                "description": "Offer description",
                "price": 9.99,
                "category": category.id,
            },
            content_type="application/json",
        )
        response_get = client.get(f"/offers/{offer.id}/")

        assert response_put.status_code == 200
        assert response_put.json()["title"] == response_get.json()["title"]
        assert response_put.json()["description"] == response_get.json()["description"]
        assert response_put.json()["price"] == response_get.json()["price"]

    def test_delete_offer(self, client):
        assert Offers.objects.count() == 0
        offers = OffersFactory.create_batch(4)
        assert Offers.objects.count() == 4

        response = client.delete(f"/offers/{offers[1].id}/")

        assert response.status_code == 204
        assert Offers.objects.count() == 3
