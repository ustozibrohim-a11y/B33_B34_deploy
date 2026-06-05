from django.urls import path

import src.frontend.views.cart as views

urlpatterns = [
    path("cart", views.cart_view, name="cart"),
    path("add-quantity/<int:item_id>", views.add_quantity, name="add_quantity"),
    path("add-to-cart/<int:product_id>", views.add_to_cart, name="add_to_cart"),
    path("remove-quantity/<int:item_id>", views.remove_quantity, name="remove_quantity"),
]
