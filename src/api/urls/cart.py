from django.urls import path

import src.api.views.cart as views

urlpatterns = [
    path("cart", views.CartView.as_view()),
    path("cart/add/", views.AddToCartView.as_view()),
    path("cart/fix/quantity/", views.FixQuantityView.as_view()),
]
