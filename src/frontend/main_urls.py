from django.urls import include, path

urlpatterns = [
    path("", include("src.frontend.urls.cart")),
    path("", include("src.frontend.urls.user")),
    path("", include("src.frontend.urls.product")),
    path("", include("src.frontend.urls.checkout")),
    path("", include("src.frontend.urls.wishlist")),
]
