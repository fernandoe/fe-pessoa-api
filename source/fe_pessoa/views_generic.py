# # -*- coding:utf-8 -*-
# import models
# from django.views.generic import ListView
# from django.views.generic.edit import FormView
# from fe_pessoa.forms import ClienteModelForm
# from django.views.generic import TemplateView
#
#
# class ClienteListView(ListView):
#     model = models.Cliente
#     template_name = 'list.html'
#     paginate_by = 15
#     list_display = ('get_uuid', 'nome', 'ativo')
#     list_section_title = 'Clientes'
#
#     def get_context_data(self, **kwargs):
#         context = super(ClienteListView, self).get_context_data(**kwargs)
#         context['list_display'] = self.list_display
#         context['list_section_title'] = self.list_section_title
#         return context
#
#
#
# class ClienteFormView(TemplateView):
#
#     template_name = 'views/edit.html'
#     # form_class = ClienteModelForm
#
#     def get_context_data(self, **kwargs):
#             context = super(ClienteFormView, self).get_context_data(**kwargs)
#             context.update(form=ClienteModelForm())
#             return context
#
#     # success_url = '/thanks/'
#
#     # def form_valid(self, form):
#     #     # This method is called when valid form data has been POSTed.
#     #     # It should return an HttpResponse.
#     #     form.send_email()
#     #     return super(ContactView, self).form_valid(form)
#
# # http://127.0.0.1:8000/admin/fe_pessoa/cliente/e052c256-6264-4a29-bb60-68ec9ebf7b8b/