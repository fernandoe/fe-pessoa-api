# -*- coding:utf-8 -*-
from django.db import models

from fe_core.models import UUIDModel, Entity


class Pessoa(UUIDModel):
    transiente = models.BooleanField(default=True, editable=False)
    entidade = models.ForeignKey(Entity)

    nome = models.CharField(max_length=128, null=True)  # Ou razão social
    cpf = models.CharField(max_length=14, null=True, blank=True)  # Ou CNPJ
    nome_fantasia = models.CharField(max_length=128, null=True, blank=True)  # somente para PJ
    contato = models.CharField(max_length=128, null=True, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    inscricao_estadual = models.CharField(max_length=20, null=True, blank=True)  # RG para PF
    inscricao_municipal = models.CharField(max_length=20, null=True, blank=True)

    endereco = models.UUIDField(null=True, blank=True)

    # Telefones
    telefone_celular = models.CharField(max_length=32, null=True, blank=True)
    telefone_comercial = models.CharField(max_length=32, null=True, blank=True)
    telefone_residencial = models.CharField(max_length=32, null=True, blank=True)
    telefone_recado = models.CharField(max_length=32, null=True, blank=True)

    site = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    observacao = models.TextField(null=True, blank=True)
    ativo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.nome

    def get_telefone(self):
        return self.telefone_celular

    def get_cpf_cnpj(self):
        return self.cpf

    class Meta:
        verbose_name = u'Pessoa'
        verbose_name_plural = u'Pessoas'
        ordering = ('nome',)


class Cliente(Pessoa):

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('cliente-details', args=[str(self.uuid).replace('-', '')])

    class Meta:
        verbose_name = u'Cliente'
        verbose_name_plural = u'Clientes'
        ordering = ('nome',)


class Fornecedor(Pessoa):

    class Meta:
        verbose_name = u'Fornecedor'
        verbose_name_plural = u'Fornecedores'
        ordering = ('nome',)
