from django.urls import path

import src.frontend.views.checkout as views

urlpatterns = [
    path("checkout", views.checkout, name="checkout")
]
