from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower

from favorites.models import Favorites
from reviews.models import Review
from .models import Product, Category, Subcategory
from .forms import ProductForm


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    total_obj = Product.objects.count()
    all_categories = Category.objects.all()
    all_subcategories = Subcategory.objects.all()
    categories = all_categories
    subcategories = all_subcategories
    subcategories_exist = None
    query = None
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
            subcategories_exist = products.filter(category__name__in=categories).values_list('subcategory__name', flat=True)

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
  
    if request.user.is_authenticated:
        context = {
            'products': products,
            'total_obj': total_obj,
            'search_term': query,
            'current_categories': categories,
            'current_subcategories': subcategories,
            'all_categories': all_categories,
            'all_subcategories': all_subcategories,
            'current_sorting': sort,
            'var_category': var_category,
            'var_subcategory': var_subcategory,
            'favorites': favorites,
            'subcategories_exist': subcategories_exist,
        }
    else:
        context = {
            'products': products,
            'total_obj': total_obj,
            'search_term': query,
            'current_categories': categories,
            'current_subcategories': subcategories,
            'all_categories': all_categories,
            'all_subcategories': all_subcategories,
            'current_sorting': sort,
            'var_category': var_category,
            'var_subcategory': var_subcategory,
            'subcategories_exist': subcategories_exist,
        }

    # PRINT VARIABLES, DON'T FORGET TO REMOVE
    # print("var_category: ", var_category)
    # print("var_subcategory: ", var_subcategory)
    print("current_categories: ", categories)
    print("current_subcategories: ", subcategories)
    print("all_categories: ", all_categories)
    print("all_subcategories: ", all_subcategories)
    print("subcategories_exist", subcategories_exist)
    # print("current_sorting: ", sort)
    # print("favorites_item", favorites_item)
    # print("favorites", favorites)

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details and the reviews"""

    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product_id)
    favorites = None

    if request.user.is_authenticated:
        try:
            favorites = Favorites.objects.get(user=request.user)
        except Favorites.DoesNotExist:
            pass

    sizes_women = range(36, 44)
    sizes_men = range(40, 47)
    sizes_kids = range(23, 36)

    context = {
        'product': product,
        'reviews': reviews,
        'sizes_women': sizes_women,
        'sizes_men': sizes_men,
        'sizes_kids': sizes_kids,
        'favorites': favorites,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
