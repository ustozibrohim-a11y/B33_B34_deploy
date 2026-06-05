from django.urls import path

import src.api.views.wishlist as views

urlpatterns = [
    path("wishlist", views.WishlistView.as_view()),
    path("wishlist/add-remove/", views.AddRemoveWishlistView.as_view())
]
