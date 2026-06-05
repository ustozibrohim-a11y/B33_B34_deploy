from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

import src.service as service
import src.core.models as models


@login_required(login_url="login")
def checkout(request):
    user = request.user
    cart = models.Cart.objects.filter(owner=user, is_active=True).last()
    items = models.CartItem.objects.filter(cart=cart)
    if len(items) == 0:
        messages.info(request, "Ilitmos kamida bitta maxsulot tanlang")
        return redirect("home")
    if request.POST:
        f_name = request.POST.get("f_name")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        ex_phone = request.POST.get("ex_phone")
        payment_type = request.POST.get("payment_type")

        billing = models.Billing.objects.create(
            f_name=f_name, address=address, phone=phone,
            ex_phone=ex_phone, payment_type=payment_type
        )
        service.OrderAddService.add_order(user, cart, items, billing)
        messages.success(request, "Buyurtmangiz saqlandi yaqin orada aloqaga chiqamiz!")
        return redirect("home")
    context = {
        "cart": cart,
        "items": items
    }
    return render(request, "checkout.html", context)
