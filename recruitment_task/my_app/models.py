from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, blank=False, unique=True)
    ordering = models.IntegerField(blank=False, unique=True)


class Offers(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=200, blank=False)
    price = models.FloatField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    category = models.ForeignKey(
        Category, related_name="category", on_delete=models.CASCADE
    )
