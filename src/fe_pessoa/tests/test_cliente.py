# -*- coding:utf-8 -*-
from django.test import TestCase
from fe_core.tests.factories import EntityFactory

from fe_pessoa.models import Cliente
from fe_pessoa.tests.factories import ClienteFactory


class TestCliente(TestCase):

    def setUp(self):
        self.cliente1 = ClienteFactory()
        self.cliente2 = ClienteFactory()
        self.entidade = EntityFactory()
        ClienteFactory.create_batch(10)

    def test_transiente(self):
        p = Cliente.objects.create(entidade=self.entidade)
        self.assertIsNotNone(p)
        self.assertTrue(p.transiente)
        p.save()
        self.assertFalse(False, p.transiente)

    def test_unicode(self):
        nome = "Fernando Espíndola"
        cliente = Cliente.objects.create(entidade=self.entidade, nome=nome)
        self.assertEqual(cliente.__unicode__(), nome)
