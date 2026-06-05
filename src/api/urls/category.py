from django.urls import path

import src.api.views.category as views

urlpatterns = [
    path("category/list", views.CategoryListAPIView.as_view())
]
