from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Subcategory


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    subcategories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            if 'subcategory' in request.GET:
                subcategories = request.GET['subcategory'].split(',')
                products = products.filter(category__name__in=categories, subcategory__name__in=subcategories)
                subcategories = Subcategory.objects.filter(name__in=subcategories)
            else:
                products = products.filter(category__name__in=categories)

            categories = Category.objects.filter(name__in=categories)


        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            # ADD DESCRIPTION TO QUERY ?????
            queries = Q(name__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_subcategories': subcategories,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)