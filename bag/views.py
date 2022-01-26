from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product


def view_bag(request):
    """ A view that renders the bag contents page """
    range_quantity = range(1, 21)
    context = {
        'range_quantity': range_quantity,
    }
    
    return render(request, 'bag/bag.html', context)


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    quantity = 1
    if 'quantity' in request.POST:
        quantity = int(request.POST.get('quantity'))

    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
                messages.success(request, f'The quantity of {product.name} size {size.upper()} is updated in your bag')
            else:
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'{product.name} size {size.upper()} is added to your bag')
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'{product.name} size {size.upper()} is added to your bag')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'The quantity of {product.name} is updatedin your bag')
        else:
            bag[item_id] = quantity
            messages.success(request, f'{product.name} is added to your bag')

    request.session['bag'] = bag

    return redirect(redirect_url)
    

def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        bag[item_id]['items_by_size'][size] = quantity
        messages.success(request, f'The quantity of {product.name} size {size.upper()} is updated in your bag')
    else:
        bag[item_id] = quantity
        messages.success(request, f'The quantity of {product.name} is updated in your bag')

    request.session['bag'] = bag

    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)

            messages.success(request, f'{product.name} size {size.upper()} is removed from your bag')

        else:
            bag.pop(item_id)
            messages.success(request, f'{product.name} is removed from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)