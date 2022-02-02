from django.contrib import admin
from .models import Favorites, FavoritesItem


class ProductInline(admin.StackedInline):
    model = FavoritesItem


class FavoritesAdmin(admin.ModelAdmin):
    inlines = [ProductInline,]


admin.site.register(Favorites, FavoritesAdmin)
