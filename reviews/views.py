from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse

from products.models import Product
from profiles.models import UserProfile
from checkout.models import Order, OrderLineItem

from .models import Review
from .forms import ReviewForm

# Defining a new custome message level
SUCCESS_NO_BAG = 50


def product_reviews(request, product_id):
    """ View to show individual product reviews"""

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
    """ View to add product review """

    product = get_object_or_404(Product, pk=product_id)
    user = get_object_or_404(UserProfile, user=request.user)
    total_product_reviews = Review.objects.filter(product=product.id).count() + 1

    # If user already submitted review for this product
    review = Review.objects.filter(product=product).filter(user=user)
    if review:
        messages.error(request, "You've already added a review for this item. You can edit your review")
        return redirect(reverse('product_detail', args=[product.id]))

    # Submit rating and review
    if request.method == 'POST':

        form_data = {
            'rating': request.POST['rating'],
            'review_text': request.POST['review_text'],
        }

        form = ReviewForm(form_data)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = user
            review.product = product
            form.save()

            messages.add_message(request, SUCCESS_NO_BAG, f'Thank you for giving a review to {product.name}!')
            
            # Update rating field on product table
            print(product.rating)
            print(total_product_reviews)
            print(review.rating)
            product.rating = (((product.rating * total_product_reviews) + review.rating) / (total_product_reviews + 1))
            product.save()

            context = {
                'product': product,
                'form': form,
            }

            return redirect(reverse('profile'))

    else:
        form = ReviewForm()

        context = {
            'product': product,
            'form': form,
            'user_profile': user,
            'review': review,
            'toast_without_bag': True,
        }

        return render(request, 'reviews/add_review.html', context)


@login_required
def edit_review(request, review_id):
    """ View to edit product review """

    review = get_object_or_404(Review, pk=review_id)
    user = get_object_or_404(UserProfile, user=request.user)

    # Check if user authenticated to edit the review
    if user.id != review.user.id:
        messages.error(request, 'You can only edit your own review')
        return render(request, 'home/index.html')

    # Submit rating and review
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.add_message(request, SUCCESS_NO_BAG, f'Your review for {review.product.name} is edited successfully')

            return redirect(reverse('product_detail', args=[review.product.id]))
        
    else:
        form = ReviewForm(instance=review)
    
    context = {
        'form': form,
        'review': review,
        'toast_without_bag': True,
    }

    return render(request, 'reviews/edit_review.html', context)


@login_required
def delete_review(request, review_id):
    """ View to delete a review """

    review = get_object_or_404(Review, pk=review_id)
    user = get_object_or_404(UserProfile, user=request.user)

    # Check if authenticated user created review being deleted
    if user.id != review.user.id:
        messages.error(request, 'You can only delete your own review')
        return render(request, 'home/index.html')

    review.delete()

    messages.add_message(request, SUCCESS_NO_BAG, 'Review successfully deleted!')
    return redirect(reverse('product_detail', args=[review.product.id]))