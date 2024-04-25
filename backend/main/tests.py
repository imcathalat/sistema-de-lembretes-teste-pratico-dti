from django.test import TestCase
from .models import Lembrete

class DatabaseConnectionTestCase(TestCase):
    def test_database_connection(self):
        try:
            lembrete = Lembrete.objects.create(nome="Entrega do teste prático da dti", data='2024-04-28')
            self.assertIsNotNone(lembrete)
        except Exception as e:
            self.fail(f"Falha ao conectar ao banco de dados: {e}")
