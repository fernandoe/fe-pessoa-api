# -*- coding:utf-8 -*-
from rest_framework import serializers

from fe_pessoa.models import Cliente, Fornecedor


class ClienteModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('uuid', 'created_at', 'updated_at', 'nome', 'email', 'telefone_celular', 'endereco')
        read_only_fields = ('uuid', 'created_at', 'updated_at')


class FornecedorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = ('uuid', 'created_at', 'updated_at', 'nome', 'telefone_celular', 'endereco')
        read_only_fields = ('uuid', 'created_at', 'updated_at')
