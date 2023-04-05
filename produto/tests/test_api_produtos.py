from rest_framework.test import APITestCase
from produto.models import Produto
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User


class ProdutosTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse("Produtos-list")
        self.user = User.objects.create_superuser(
            email="test@test.com", password="123456", username="Usuário Teste"
        )
        self.client.force_authenticate(self.user)
        self.produto_um = Produto.objects.create(nome="Produto Teste 1", tipo="KIT")
        self.produto_um = Produto.objects.create(nome="Produto Teste 2", tipo="EVENTO")

    def test_get_produtos(self):
        resposta = self.client.get(self.list_url)
        self.assertEqual(resposta.status_code, status.HTTP_200_OK)
