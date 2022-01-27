from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Favorites(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(
        Product, default="", through='FavoritesItem')

    def __str__(self):
        return f'Favorites ({self.user})'


class FavoritesItem(models.Model):
    favorites = models.ForeignKey(
        Favorites, null=False, blank=False, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product.id)
