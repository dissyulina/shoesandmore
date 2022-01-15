from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Subcategory


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    sort = None
    direction = None
    var_category = None
    var_subcategory = None

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

    current_sorting = f'{sort}_{direction}'
  
    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_subcategories': subcategories,
        'current_sorting': sort,
        'var_category': var_category,
        'var_subcategory': var_subcategory,
    }

    # PRINT VARIABLES, DON'T FORGET TO REMOVE
    print("var_category: ", var_category)
    print("var_subcategory: ", var_subcategory)
    print("current_categories: ", categories)
    print("current_subcategories: ", subcategories)
    print("current_sorting: ", sort)

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)