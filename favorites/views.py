from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect

from products.models import Product
from profiles.models import UserProfile
from favorites.models import Favorites, FavoritesItem


# Defining a new custome message level
SUCCESS_NO_BAG = 50

# Source: modified from a slack thread, conversation between Joe2308 and ckz8780
@login_required()
def view_favorites(request):
    """ A view that renders the favorites contents page """
 
    favorites = None
    try:
        favorites = Favorites.objects.get(user=request.user)
    except Favorites.DoesNotExist:
        pass
    
    sizes_women = range(36, 44)
    sizes_men = range(40, 47)
    sizes_kids = range(23, 36)

    context = {
        'favorites': favorites,
        'sizes_women': sizes_women,
        'sizes_men': sizes_men,
        'sizes_kids': sizes_kids,
    }

    return render(request, 'favorites/favorites.html', context=context)


@login_required()
def add_to_favorites(request, item_id):
    """ Add a specified product to the favorites """

    product = get_object_or_404(Product, pk=item_id)
    favorites, created = Favorites.objects.get_or_create(user=request.user)

    if FavoritesItem.objects.filter(favorites=favorites, product=product).exists():
    # if product in favorites.products.all():
        messages.error(request, f'{product.name} is already in your favorites')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    else:
        favorites.products.add(product)
        messages.add_message(request, SUCCESS_NO_BAG, f'{product.name} is added to your favorites')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
    return redirect(redirect_url)


@login_required()
def remove_from_favorites(request, item_id):
    """ Remove a specified product to the favorites """

    product = get_object_or_404(Product, pk=item_id)
    favorites = Favorites.objects.get(user=request.user)
    
    favorites.products.remove(product)
    messages.add_message(request, SUCCESS_NO_BAG, f'{product.name} is removed from your favorites')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])