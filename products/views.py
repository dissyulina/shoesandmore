from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.core import serializers
from django.http import JsonResponse
from django.db.models import Q
from django.db.models.functions import Lower

from favorites.models import Favorites, FavoritesItem
from reviews.models import Review
from .models import Product, Category, Subcategory



def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    total_obj = Product.objects.count()
    query = None
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    sort = None
    direction = None
    var_category = None
    var_subcategory = None
    favorites = None

    if request.user.is_authenticated:
        try:
            favorites = Favorites.objects.get(user=request.user)
        except Favorites.DoesNotExist:
            pass

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            var_category = request.GET['category']
            categories = request.GET['category'].split(',')

            if 'subcategory' in request.GET:
                var_subcategory = request.GET['subcategory']
                subcategories = request.GET['subcategory'].split(',')
                products = products.filter(category__name__in=categories, subcategory__name__in=subcategories)
                subcategories = Subcategory.objects.filter(name__in=subcategories)

            else:
                products = products.filter(category__name__in=categories)

            categories = Category.objects.filter(name__in=categories)

        if 'subcategory' in request.GET:
            var_subcategory = request.GET['subcategory']
            subcategories = request.GET['subcategory'].split(',')
            products = products.filter(subcategory__name__in=subcategories)
            subcategories = Subcategory.objects.filter(name__in=subcategories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            # ADD DESCRIPTION TO QUERY ?????
            queries = Q(name__icontains=query)
            products = products.filter(queries)

    else:
        products = products[0:24]

    current_sorting = f'{sort}_{direction}'
  
    if request.user.is_authenticated:
        context = {
            'products': products,
            'total_obj': total_obj,
            'search_term': query,
            'current_categories': categories,
            'current_subcategories': subcategories,
            'current_sorting': sort,
            'var_category': var_category,
            'var_subcategory': var_subcategory,
            'favorites': favorites,
        }
    else:
        context = {
            'products': products,
            'total_obj': total_obj,
            'search_term': query,
            'current_categories': categories,
            'current_subcategories': subcategories,
            'current_sorting': sort,
            'var_category': var_category,
            'var_subcategory': var_subcategory,
        }

    # PRINT VARIABLES, DON'T FORGET TO REMOVE
    # print("var_category: ", var_category)
    # print("var_subcategory: ", var_subcategory)
    # print("current_categories: ", categories)
    # print("current_subcategories: ", subcategories)
    # print("current_sorting: ", sort)
    # print("favorites_item", favorites_item)
    print("favorites", favorites)

    return render(request, 'products/products.html', context)


def load_more(request):
    """Load more products"""

    loaded_item = request.GET.get('loaded_item')
    loaded_item_int = int(loaded_item)
    limit = 12
    product_obj = list(Product.objects.values()[loaded_item_int:loaded_item_int+limit])
    loaded_item_after = loaded_item_int + limit
    data = {
        'products': product_obj,
        'loaded_item_after': loaded_item_after
    }
    print(loaded_item_after)
    return JsonResponse(data=data)


def product_detail(request, product_id):
    """ A view to show individual product details and the reviews"""

    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product__id__in=product_id)

    sizes_women = range(36, 44)
    sizes_men = range(40, 47)
    sizes_kids = range(23, 36)

    context = {
        'product': product,
        'reviews': reviews,
        'sizes_women': sizes_women,
        'sizes_men': sizes_men,
        'sizes_kids': sizes_kids,
    }

    return render(request, 'products/product_detail.html', context)

