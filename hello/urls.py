from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("maaz", views.maaz, name='maaz'),
    path("<str:name>", views.greet, name="greet")

]