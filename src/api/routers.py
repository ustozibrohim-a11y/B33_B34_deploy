from django.urls import path, include

urlpatterns = [
    path("", include("src.api.urls.cart")),
    path("", include("src.api.urls.user")),
    path("", include("src.api.urls.order")),
    path("", include("src.api.urls.product")),
    path("", include("src.api.urls.category")),
    path("", include("src.api.urls.wishlist")),
]
