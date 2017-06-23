# -*- coding:utf-8 -*-
from django.contrib import admin

from fe_pessoa.models import Cliente


@admin.register(Cliente)
class ClienteModelAdmin(admin.ModelAdmin):
    search_fields = ('nome', 'cpf', 'cnpj',)
    list_display = ('get_uuid', 'entidade', 'nome', 'telefone_celular', 'ativo')
    ordering = ('nome',)

    def save_model(self, request, obj, form, change):
        obj.transiente = False
        super(ClienteModelAdmin, self).save_model(request, obj, form, change)
