from django.db import models


class Category(models.Model):
    """ Category Model (Women, Men, Kids) """

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Subcategory(models.Model):
    """ Subcategory Model (e.g. Sneakers, Boots, Sale, etc)"""

    class Meta:
        verbose_name_plural = 'Subcategories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """ Product Model """

    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    subcategory = models.ForeignKey('Subcategory', null=True, blank=True,
                                    on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, default=3,
                                 null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    total_purchased = models.IntegerField(default=0, null=False, blank=False)

    def __str__(self):
        return self.name
