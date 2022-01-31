from django.shortcuts import render, get_object_or_404
from products.models import Product 


def product_reviews(request, product_id):
    """ A view to show individual product reviews"""

    reviews = get_object_or_404(Reviews, pk=product_id)
    context = {
        'reviews': reviews,
    }
    return render(request, 'reviews/product_reviews.html', context)


def add_review(request, product_id):
    """ A view to add product review """

    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }

    return render(request, 'reviews/add_review.html', context)