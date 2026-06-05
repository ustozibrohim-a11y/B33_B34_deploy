from django.urls import path

import src.frontend.views.product as views

urlpatterns = [
    path("", views.home, name="home"),
    path("product/list/search", views.product_searched_list, name="search"),
    path("write/comments/<int:product_id>", views.write_comments, name="write_comment"),
    path("filter/category/<int:category_id>", views.product_filter_by_category, name="category_by")
]
