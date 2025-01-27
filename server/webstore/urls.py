from . import views
from django.urls import path

urlpatterns = [
    path("", views.main, name="landing"),
    path("<int:product_id>", views.detail, name="detail"),
    path("login", views.login, name="login"),
]