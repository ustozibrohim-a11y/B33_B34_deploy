from django.urls import path

import src.api.views.product as views

urlpatterns = [
    path("product/list", views.ProductListAPIView.as_view()),
    path("comments/list", views.CommentsListAPIView.as_view()),
    path("comments/write", views.WriteCommentAPIView.as_view()),
    path("product/detail/<int:pk>", views.ProductDetailAPIView.as_view())
]
