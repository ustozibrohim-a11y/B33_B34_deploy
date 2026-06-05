from django.urls import path

import src.frontend.views.wishlist as views

urlpatterns = [
    path("wishlist", views.wishlist, name="wishlist"),
    path("add-remove-wishlist/<int:product_id>", views.add_remove_wishlist, name="wishlist_ctl")
]
