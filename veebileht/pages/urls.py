from django.urls import path
from . import views
urlpatterns = [
    path("home/", views.home, name="home"),
    path("add/", views.add, name="add"),
    path("subst/", views.subst, name="subst"),
]
