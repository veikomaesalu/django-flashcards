from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("add.html", views.add, name="add"),
]
