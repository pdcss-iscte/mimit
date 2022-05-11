from django.urls import include, path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path('guardarregistoutilizador/', views.guardarregistoutilizador, name="guardarregistoutilizador")

]
