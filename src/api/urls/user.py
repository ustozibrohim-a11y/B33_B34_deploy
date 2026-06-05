from django.urls import path

import src.api.views.user as views

urlpatterns = [
    path("user/me", views.GetMeView.as_view()),
    path("user/register", views.UserRegisterView.as_view()),
]
