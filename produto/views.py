from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, status
from rest_framework.response import Response

from produto.models import Produto
from produto.serializers import ProdutoSerializer


class ProdutosViewSet(viewsets.ModelViewSet):
    """API de Produtos"""

    queryset = Produto.objects.all()
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["nome"]
    search_fields = ["nome", "cpf"]
    serializer_class = ProdutoSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            id = str(serializer.data.get("id"))
            response["Location"] = request.build_absolute_uri() + id
            return response
