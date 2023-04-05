from rest_framework.test import APITestCase
from produto.models import Produto
from produto.serializers import ProdutoSerializer


class ProdutoSerializerTestCase(APITestCase):
    def setUp(self):
        self.produto = Produto(
            nome="Produto Serializado",
        )
        self.serializer = ProdutoSerializer(instance=self.produto)

    def test_valida_campos_serializados(self):
        dados = self.serializer.data
        self.assertEqual(set(dados.keys()), set(["id", "nome", "tipo"]))

    def test_valida_valores_dos_campos_serializados(self):
        dados = self.serializer.data
        self.assertEqual(dados.get("id"), str(self.produto.id))
        self.assertEqual(dados.get("nome"), self.produto.nome)
        self.assertEqual(dados.get("tipo"), self.produto.tipo)
