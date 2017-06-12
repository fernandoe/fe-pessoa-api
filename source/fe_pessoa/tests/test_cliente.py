# -*- coding:utf-8 -*-
import uuid

from django.test import TestCase

from fe_pessoa.models import Cliente
from fe_pessoa.tests.factories import ClienteFactory


class TestCliente(TestCase):

    def setUp(self):
        self.cliente1 = ClienteFactory()
        self.cliente2 = ClienteFactory()
        ClienteFactory.create_batch(10)

    def test_transiente(self):
        p = Cliente.objects.create(entidade=uuid.uuid4())
        self.assertIsNotNone(p)
        self.assertTrue(p.transiente)
        p.save()
        self.assertFalse(False, p.transiente)

    def test_unicode(self):
        nome = "Fernando Espíndola"
        cliente = Cliente.objects.create(entidade=uuid.uuid4(), nome=nome)
        self.assertEqual(cliente.__unicode__(), nome)
