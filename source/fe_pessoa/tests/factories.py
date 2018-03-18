# -*- coding:utf-8 -*-
import uuid

import factory
from fe_core.tests.factories import EntityFactory

from fe_pessoa.models import Cliente, Fornecedor


class FornecedorFactory(factory.django.DjangoModelFactory):
    uuid = factory.Sequence(lambda n: uuid.uuid4())
    nome = factory.Faker('name', locale='pt_BR')
    email = factory.Faker('email', locale='pt_BR')
    entidade = factory.SubFactory(EntityFactory)
    transiente = False

    class Meta:
        model = Fornecedor


class ClienteFactory(factory.django.DjangoModelFactory):
    uuid = factory.Sequence(lambda n: uuid.uuid4())
    nome = factory.Faker('name', locale='pt_BR')
    email = factory.Faker('email', locale='pt_BR')
    entidade = factory.SubFactory(EntityFactory)
    transiente = False

    class Meta:
        model = Cliente


class ClienteFernandoFactory(factory.django.DjangoModelFactory):
    uuid = factory.Sequence(lambda n: uuid.uuid4())
    nome = 'Fernando Espíndola'
    email = 'fer.esp@gmail.com'
    entidade = factory.Sequence(lambda n: uuid.uuid4())
    transiente = False

    class Meta:
        model = Cliente
