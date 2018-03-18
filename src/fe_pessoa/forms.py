# # -*- coding:utf-8 -*-
# import logging
#
# from django.conf import settings
# from django import forms
#
# from fe_pessoa.models import Cliente, Pessoa, Fornecedor
#
#
# logger = logging.getLogger(settings.APP_LOOGER)
#
#
# class PessoaModelForm(forms.ModelForm):
#     class Meta:
#         model = Pessoa
#         exclude = ('empresa', 'usuario')
#
#
# class ClienteModelForm(forms.ModelForm):
#     class Meta:
#         model = Cliente
#         fields = ('nome', 'cpf', 'data_nascimento', 'telefone_celular_ddd', 'telefone_celular')
#         # exclude = ('empresa', 'usuario')
#
#
# class FornecedorModelForm(forms.ModelForm):
#     class Meta:
#         model = Fornecedor
#         exclude = ('empresa', 'usuario')
