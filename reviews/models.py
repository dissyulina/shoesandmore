from django.db import models
from django.contrib.auth.models import User

from products.models import Product
from profiles.models import UserProfile


class Review(models.Model):

    RATINGS = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]

    rating = models.IntegerField(choices=RATINGS)
    reviews = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserProfile, null=False, blank=False, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
