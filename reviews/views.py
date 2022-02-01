from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse

from products.models import Product
from profiles.models import UserProfile
from checkout.models import Order, OrderLineItem

from .models import Review

from .forms import ReviewForm


def product_reviews(request, product_id):
    """ A view to show individual product reviews"""

    #reviews = get_object_or_404(Review, pk=product_id)
    reviews = Review.objects.filter(product__id__in=product_id)

    product = get_object_or_404(Product, pk=product_id)
    
    context = {
        'reviews': reviews,
        'product': product,
    }
    print(reviews)
    return render(request, 'reviews/product_reviews.html', context)


@login_required
def add_review(request, product_id):
    """ A view to add product review """

    product = get_object_or_404(Product, pk=product_id)
    user = get_object_or_404(UserProfile, user=request.user)

    # If user already submitted review for this product
    review = Review.objects.filter(product=product).filter(user=user)
    if review:
        messages.error(request, "You've already added a review for this item. You can edit your review")
        return render(request, 'home/index.html')

    # Submit rating and review
    if request.method == 'POST':

        form_data = {
            'rating': request.POST['rating'],
            'review_text': request.POST['review_text'],
        }
        print(form_data)
        form = ReviewForm(form_data)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = user
            review.product = product
            form.save()
            print(form)
            messages.success(request, f'Your review for {product.name} is added successfully')

            context = {
                'product': product,
                'form': form,
            }

            return redirect(reverse('product_detail', args=[product.id]))
        
    else:
        form = ReviewForm()

        context = {
            'product': product,
            'form': form,
            'user_profile': user,
            'review': review,
            'on_review_page': True,
        }

        return render(request, 'reviews/add_review.html', context)