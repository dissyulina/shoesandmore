from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product


def view_favorites(request):
    """ A view that renders the favorites contents page """

    return render(request, 'favorites/favorites.html')
