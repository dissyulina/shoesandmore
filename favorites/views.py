from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product
# from profiles.models import UserProfile
from favorites.models import Favorites, FavoritesItem

# source: Python Django Ecommerce Customer Wishlist video https://www.youtube.com/watch?v=OgA0TTKAtqQ&t=138s 

def view_favorites(request):
    """ A view that renders the favorites contents page """

    favorites = None
    # profile = get_object_or_404(UserProfile, user=request.user)
    try:
        favorites = Favorites.objects.get(user=profile)
    except Favorites.DoesNotExist:
        pass

    context = {
        'favorites': favorites,
    }

    return render(request, 'favorites/favorites.html', context=context)


def add_to_favorites(request, item_id):
    """ Add a specified product to the favorites """

    product = get_object_or_404(Product, pk=item_id)

    if request.method =='POST':
        favorites, created = Favorites.objects.get_or_create(user=request.user)
    
        if WishlistItem.objects.filter(wishlist=wishlist, product=product).exists():
            messages.error(request, f'{product.name} is removed from your favorites')
            return redirect(reverse('product_detail', args=[product.id]))

        else:
            wishlist.products.add(product)
            messages.success(request, f'{product.name} is added to your favorites')
            return redirect(reverse('product_detail', args=[product.id]))
            
    return redirect(redirect_url)

