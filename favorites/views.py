from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect

from products.models import Product
from profiles.models import UserProfile
from favorites.models import Favorites, FavoritesItem

# source: Python Django Ecommerce Customer Wishlist video https://www.youtube.com/watch?v=OgA0TTKAtqQ&t=138s 

@login_required()
def view_favorites(request):
    """ A view that renders the favorites contents page """

    favorites = None

    try:
        favorites = Favorites.objects.get(user=request.user)
    except Favorites.DoesNotExist:
        pass

    context = {
        'favorites': favorites,
    }

    return render(request, 'favorites/favorites.html', context=context)


@login_required()
def add_to_favorites(request, item_id):
    """ Add a specified product to the favorites """

    product = get_object_or_404(Product, pk=item_id)
    favorites, created = Favorites.objects.get_or_create(user=request.user)

    if FavoritesItem.objects.filter(favorites=favorites, product=product).exists():
        messages.error(request, f'{product.name} is already in your wishlist')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    else:
        favorites.products.add(product)
        messages.success(request, f'{product.name} is added to your favorites')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
    return redirect(redirect_url)

