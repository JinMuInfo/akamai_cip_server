from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.return_200),
    re_path(r'^es$', views.lookup_ip),
]
