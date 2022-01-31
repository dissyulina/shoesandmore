from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from products.models import Product
from profiles.models import UserProfile


def product_reviews(request, product_id):
    """ A view to show individual product reviews"""

    reviews = get_object_or_404(Reviews, pk=product_id)
    context = {
        'reviews': reviews,
    }
    return render(request, 'reviews/product_reviews.html', context)


@login_required
def add_review(request, product_id):
    """ A view to add product review """

    product = get_object_or_404(Product, pk=product_id)
    user = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form_data = {
            'ratings': request.POST['ratings'],
            'comments': request.POST['comments'],
        }

    context = {
        'product': product,
    }

    return render(request, 'reviews/add_review.html', context)