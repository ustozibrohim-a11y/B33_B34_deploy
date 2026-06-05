from django.urls import path

import src.api.views.order as views

urlpatterns = [
    path("billing", views.OrderAPIView.as_view())
]
