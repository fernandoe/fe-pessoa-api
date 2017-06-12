# import uuid
#
# from django.core.cache import cache
# from django.core.urlresolvers import reverse
# from django.test import TestCase
# from rest_framework import status
# from rest_framework.test import APIClient
#
# from fe_core.tests.factories import TokenFactory
# from fe_pessoa.models import Cliente
# from fe_pessoa.tests.factories import ClienteFactory
#
#
# class TestClienteViewSet(TestCase):
#
#     def compare_entity(self, entity, result):
#         self.assertEqual(6, len(result))
#         self.assertEqual(str(entity.uuid), result.get('uuid'))
#         self.assertTrue(result.get('created_at', None))
#         self.assertTrue(result.get('updated_at', None))
#         self.assertEqual(entity.nome, result.get('nome'))
#         self.assertEqual(entity.telefone_celular, result.get('telefone_celular'))
#         self.assertEqual(str(entity.endereco), result.get('endereco'))
#
#     def setUp(self):
#         token = TokenFactory()
#         self.entidade = token.entidade
#         cache.set(token.key, token.to_json())
#         self.client = APIClient()
#         self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(token.key))
#         self.pessoa = str(uuid.uuid4())
#         self.cliente = ClienteFactory(entidade=self.entidade)
#
#     def test_get(self):
#         response = self.client.get(reverse('clientes-list'))
#         # print "STATUS CODE: %s - RESPONSE: %s" % (response.status_code, response.content)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(1, response.data.get('count'))
#
#     def test_get_transiente_true(self):
#         cliente = ClienteFactory(entidade=self.entidade, transiente=True)
#         response = self.client.get(reverse('clientes-detail', args=(cliente.uuid,)))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         # print "STATUS CODE: %s - RESPONSE: %s" % (response.status_code, response.content)
#         self.assertEqual(str(cliente.uuid), response.data.get('uuid'))
#         self.assertTrue(cliente.transiente)
#
#     def test_get_transiente_false(self):
#         cliente = ClienteFactory(entidade=self.entidade, transiente=False)
#         response = self.client.get(reverse('clientes-detail', args=(cliente.uuid,)))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         # print "STATUS CODE: %s - RESPONSE: %s" % (response.status_code, response.content)
#         self.assertEqual(str(cliente.uuid), response.data.get('uuid'))
#         self.assertFalse(cliente.transiente)
#
#     def test_post(self):
#         response = self.client.post(reverse('clientes-list'), {
#             'nome': 'Cliente de teste (post)',
#             'telefone_celular': '92832466',
#             'endereco': str(uuid.uuid4())
#         })
#         # print "STATUS CODE: %s - RESPONSE: %s" % (response.status_code, response.content)
#         self.assertEqual(status.HTTP_201_CREATED, response.status_code)
#         entity = Cliente.objects.get(pk=response.data.get('uuid'))
#         result = response.data
#         self.compare_entity(entity, result)
#         self.assertEqual(self.entidade, str(entity.entidade))
#         self.assertFalse(entity.transiente)
#
#     def test_put(self):
#         cliente = Cliente.objects.create(entidade=self.entidade)
#         self.assertTrue(cliente.transiente)
#         response = self.client.put(reverse('clientes-detail', args=(cliente.uuid,)), {
#             'nome': 'Cliente de teste (put)',
#             'telefone_celular': '92832466',
#             'endereco': str(uuid.uuid4())
#         })
#         # print "STATUS CODE: %s - RESPONSE: %s" % (response.status_code, response.content)
#         self.assertEqual(status.HTTP_200_OK, response.status_code)
#         entity = Cliente.objects.get(pk=response.data.get('uuid'))
#         result = response.data
#         self.compare_entity(entity, result)
#         self.assertEqual(self.entidade, str(entity.entidade))
#         self.assertFalse(entity.transiente)
#
#     def test_patch_endereco(self):
#         endereco = str(uuid.uuid4())
#         response = self.client.patch(reverse('clientes-detail', args=(self.cliente.uuid,)), {
#             'endereco': endereco
#         })
#         # print "STATUS CODE: %s - RESPONSE: %s" % (response.status_code, response.content)
#         entity = Cliente.objects.get(pk=response.data.get('uuid'))
#         self.assertEqual(endereco, response.data.get('endereco'))
#         self.assertEqual(endereco, str(entity.endereco))
#
#     def test_uudis(self):
#         cliente1 = ClienteFactory(entidade=self.entidade)
#         cliente2 = ClienteFactory(entidade=self.entidade)
#         ClienteFactory(entidade=self.entidade, transiente=True)
#         ClienteFactory.create_batch(3)
#         uuids = '%s,%s' % (cliente1.uuid, cliente2.uuid)
#         response = self.client.get(reverse('clientes-list'), {
#             'uuids': uuids
#         })
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         # print "STATUS CODE: %s - RESPONSE: %s" % (response.status_code, response.content)
#         self.assertEqual(2, response.data.get('count'))
#         results = response.data.get('results')
#         self.assertEqual(str(cliente1.uuid), results[0].get('uuid'))
#         self.assertEqual(str(cliente2.uuid), results[1].get('uuid'))
#
#     def test_query(self):
#         cliente = ClienteFactory(nome="Cliente (123)", entidade=self.entidade)
#         ClienteFactory(entidade=self.entidade, transiente=True)
#         ClienteFactory.create_batch(3)
#         response = self.client.get(reverse('clientes-list'), {
#             'query': '123'
#         })
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         # print "STATUS CODE: %s - RESPONSE: %s" % (response.status_code, response.content)
#         self.assertEqual(1, response.data.get('count'))
#         results = response.data.get('results')
#         self.assertEqual(str(cliente.uuid), results[0].get('uuid'))
#         self.assertEqual(str(cliente.nome), results[0].get('nome'))
