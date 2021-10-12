import pytest

from my_app.models import Category
from my_app.tests.factories import CategoryFactory


@pytest.mark.django_db
class TestCategory:
    def test_create_category(self, client):
        assert Category.objects.count() == 0
        response = client.post("/category/", {"name": "Category1", "ordering": 1})

        assert response.status_code == 201
        assert Category.objects.count() == 1
        assert response.json()["id"] == 1
        assert response.json()["name"] == "Category1"
        assert response.json()["ordering"] == 1

    def test_list_category(self, client):
        CategoryFactory.create_batch(5)

        response = client.get("/category/")

        assert response.status_code == 200
        assert len(response.json()) == 5

    def test_detail_category(self, client):
        category = CategoryFactory()

        response = client.get(f"/category/{category.id}/")

        assert response.status_code == 200
        assert response.json()["name"] == category.name

    def test_update_category(self, client):
        category = CategoryFactory()

        response_put = client.put(
            f"/category/{category.id}/",
            {"name": "Category1", "ordering": 1},
            content_type="application/json",
        )
        response_get = client.get(f"/category/{category.id}/")
        assert response_put.status_code == 200
        assert response_put.json()["name"] == response_get.json()["name"]

    def test_delete_category(self, client):
        assert Category.objects.count() == 0
        categories = CategoryFactory.create_batch(4)
        assert Category.objects.count() == 4

        response = client.delete(f"/category/{categories[1].id}/")

        assert response.status_code == 204
        assert Category.objects.count() == 3
