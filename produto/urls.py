from django.urls import path, include
from rest_framework import routers

from produto.views import ProdutosViewSet

produto = routers.DefaultRouter()
produto.register("produtos", ProdutosViewSet, basename="Produtos")


urlpatterns = [path("", include(produto.urls))]
