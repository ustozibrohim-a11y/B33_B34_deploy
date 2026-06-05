from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

import src.core.models as models


@login_required(login_url="login")
def cart_view(request):
    user = request.user
    cart, created = models.Cart.objects.get_or_create(owner=user, is_active=True)
    items = models.CartItem.objects.filter(cart=cart)
    context = {
        "cart": cart,
        "items": items
    }
    return render(request, "cart.html", context)


@login_required(login_url="login")
def add_to_cart(request, product_id):
    user = request.user
    cart, created = models.Cart.objects.get_or_create(owner=user, is_active=True)
    product = get_object_or_404(models.Product, pk=product_id)
    item, created = models.CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += 1
        item.save()
    cart.calculate_total()
    messages.info(request, "Cart item saved")
    return redirect("home")

    # if models.Cart.objects.filter(owner=user, is_active=True).exists():
    #     cart = models.Cart.objects.filter(owner=user, is_active=True).last()  # [item][0] -> item
    # else:
    #     cart = models.Cart.objects.create(owner=user)
    # if models.CartItem.objects.filter(cart=cart, product=product).exists():
    #     item = models.CartItem.objects.filter(cart=cart, product=product).last()
    #     item.quantity += 1
    #     item.save()
    # else:
    #     models.CartItem.objects.create(cart=cart, product=product)


@login_required(login_url="login")
def add_quantity(request, item_id):
    item = get_object_or_404(models.CartItem, pk=item_id)
    item.quantity += 1
    item.save()
    item.cart.calculate_total()
    return redirect("cart")


@login_required(login_url="login")
def remove_quantity(request, item_id):
    item = get_object_or_404(models.CartItem, pk=item_id)
    cart = get_object_or_404(models.Cart, pk=item.cart.pk)
    item.quantity -= 1
    if item.quantity == 0:
        item.delete()
    else:
        item.save()
    cart.calculate_total()
    return redirect("cart")
