# -*- coding:utf-8 -*-
import uuid

import factory
from fe_core.tests.factories import EntityFactory

from fe_pessoa.models import Cliente, Fornecedor


class FornecedorFactory(factory.django.DjangoModelFactory):
    uuid = factory.Sequence(lambda n: uuid.uuid4())
    nome = factory.Sequence(lambda n: 'Fornecedor de Teste => 00{0}'.format(n))
    entidade = factory.SubFactory(EntityFactory)
    transiente = False

    class Meta:
        model = Fornecedor


class ClienteFactory(factory.django.DjangoModelFactory):
    uuid = factory.Sequence(lambda n: uuid.uuid4())
    nome = factory.Sequence(lambda n: 'Cliente de Teste => 00{0}'.format(n))
    entidade = factory.SubFactory(EntityFactory)
    transiente = False

    class Meta:
        model = Cliente


class ClienteFernandoFactory(factory.django.DjangoModelFactory):
    uuid = factory.Sequence(lambda n: uuid.uuid4())
    nome = 'Fernando Espíndola'
    entidade = factory.Sequence(lambda n: uuid.uuid4())
    transiente = False

    class Meta:
        model = Cliente