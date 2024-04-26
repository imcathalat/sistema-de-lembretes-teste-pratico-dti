from django.urls import reverse
from rest_framework import status

from django.test import TestCase
from .models import Lembrete
from .serializers import LembreteSerializer

class DatabaseConnectionTestCase(TestCase):
    def test_database_connection(self):
        try:
            lembrete = Lembrete.objects.create(
                nome="Entrega do teste prático da dti", 
                data='2024-04-28'
            )

            self.assertIsNotNone(lembrete)
        except Exception as e:
            self.fail(f"Falha ao conectar ao banco de dados: {e}")


class LembretesViewTestCase(TestCase):

    def setUp(self):
        self.lembrete = Lembrete.objects.create(
            nome='Entrega do teste prático da dti',
            data='2024-04-28'
        )

    def test_get_queryset_lembretes(self):
        #testa se o método get da view LembreteList funciona corretamente
        url = reverse('lembretes')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        #testa se o serializer pega os objetos do LembreteSerializer corretamente
        serializer_data = LembreteSerializer([self.lembrete], many=True).data
        self.assertEqual(response.data, serializer_data)

    def test_create_lembrete(self):
        url = reverse('lembretes')
        data = {
            "nome": "show da madona no rj",
            "data": "2024-04-05"
        }
        response = self.client.post(url, data)

        serializer = LembreteSerializer(data=data)
        self.assertTrue(serializer.is_valid())

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
