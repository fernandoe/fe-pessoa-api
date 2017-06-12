# # -*- coding:utf-8 -*-
# from django.conf.urls import patterns, url
#
# urlpatterns = []
# # urlpatterns = patterns(
# #     'fe_pessoa.views.view_cliente',
# #
# #     url(r'^clientes/$', 'api_pessoa_cliente', name="api_pessoa_cliente"),
# #     url(r'^clientes/(?P<uuid>[0-9a-f]{32})/$', 'api_pessoa_cliente', name="api_pessoa_cliente"),
# # )
#
# # # -*- coding:utf-8 -*-
# # from django.conf.urls import url
# #
# from fe_pessoa.views_generic import ClienteListView, ClienteFormView
#
# urlpatterns += [
#     url(r'^clientes/$', ClienteListView.as_view(), name='cliente-list'),
#     url(r'^clientes/(?P<uuid>[0-9a-f]{32})/$', ClienteFormView.as_view(), name="cliente-persist"),
# ]
