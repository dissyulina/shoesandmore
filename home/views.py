from django.shortcuts import render

from blogs.models import Blog
from products.models import Product
from favorites.models import Favorites


def index(request):
    """ Home Page """

    products = Product.objects.all().order_by('-total_purchased')[0:8]
    blogs = Blog.objects.all().order_by('-created_on')[0:3]

    favorites = None
    if request.user.is_authenticated:
        try:
            favorites = Favorites.objects.get(user=request.user)
        except Favorites.DoesNotExist:
            pass

    context = {
        'blogs': blogs,
        'products': products,
        'favorites': favorites,
    }

    return render(request, 'home/index.html', context)
