from django.shortcuts import render, get_object_or_404
from products.models import Product 


def product_reviews(request, product_id):
    """ A view to show individual product reviews"""

    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }

    return render(request, 'reviews/product_reviews.html', context)