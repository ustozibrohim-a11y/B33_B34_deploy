from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

import src.core.models as models


@login_required(login_url="login")
def add_remove_wishlist(request, product_id):
    user = request.user
    product = get_object_or_404(models.Product, pk=product_id)
    if models.Wishlist.objects.filter(user=user, product=product).exists():
        messages.info(request, "Wishlist item deleted")
        models.Wishlist.objects.filter(user=user, product=product).delete()
    else:
        messages.success(request, "Wishlist item added")
        models.Wishlist.objects.create(user=user, product=product)
    return redirect("home")


@login_required(login_url="login")
def wishlist(request):
    user = request.user
    likes = models.Wishlist.objects.filter(user=user)
    product_ids = []
    for i in likes:
        product_ids.append(i.product.pk)
    object_list = models.Product.objects.filter(id__in=product_ids)
    context = {
        "object_list": object_list
    }
    return render(request, "home.html", context)
