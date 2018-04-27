from django.contrib import admin

from fe_pessoa.models import Cliente


@admin.register(Cliente)
class ClienteModelAdmin(admin.ModelAdmin):
    search_fields = ('uuid', 'nome', 'cpf',)
    list_filter = ['transiente']
    list_display = ('get_uuid', 'entidade', 'nome', 'email', 'telefone_celular', 'ativo', 'transiente', 'endereco')
    ordering = ('nome',)

    def save_model(self, request, obj, form, change):
        obj.transiente = False
        super(ClienteModelAdmin, self).save_model(request, obj, form, change)
