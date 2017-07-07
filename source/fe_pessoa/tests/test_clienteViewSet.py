# import uuid
#
# from django.core.urlresolvers import reverse
# from django.test import TestCase
# from fe_core.tests.factories import AccessTokenFactory, EntityFactory, UserFactory
# from rest_framework import status
# from rest_framework.test import APIClient
#
# from fe_pessoa.models import Cliente
# from fe_pessoa.tests.factories import ClienteFactory
#
#
# class TestClienteViewSet(TestCase):
#     def setUp(self):
#         self.entity = EntityFactory()
#         self.user = UserFactory(entity=self.entity)
#         access_token = AccessTokenFactory(user=self.user)
#         self.client = APIClient()
#         self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(access_token.token))
#         self.pessoa = str(uuid.uuid4())
#         self.cliente = ClienteFactory(entidade=self.entity)
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
#     def test_get_200(self):
#         response = self.client.get(reverse('clientes-list'))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(1, len(response.data))
#
#     def test_get_transiente_true(self):
#         cliente = ClienteFactory(entidade=self.entity, transiente=True)
#         response = self.client.get(reverse('clientes-detail', args=(cliente.uuid,)))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(str(cliente.uuid), response.data.get('uuid'))
#         self.assertTrue(cliente.transiente)
#
#     def test_get_transiente_false(self):
#         cliente = ClienteFactory(entidade=self.entity, transiente=False)
#         response = self.client.get(reverse('clientes-detail', args=(cliente.uuid,)))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(str(cliente.uuid), response.data.get('uuid'))
#         self.assertFalse(cliente.transiente)
#
#     def test_put(self):
#         cliente = Cliente.objects.create(entidade=self.entity)
#         self.assertTrue(cliente.transiente)
#         response = self.client.put(reverse('clientes-detail', args=(cliente.uuid,)), {
#             'nome': 'Cliente de teste (put)',
#             'telefone_celular': '92832466',
#             'endereco': str(uuid.uuid4())
#         })
#         self.assertEqual(status.HTTP_200_OK, response.status_code)
#         entity = Cliente.objects.get(pk=response.data.get('uuid'))
#         result = response.data
#         self.compare_entity(entity, result)
#         self.assertEqual(self.entity, entity.entidade)
#         self.assertFalse(entity.transiente)
#
#     def test_patch_endereco(self):
#         endereco = str(uuid.uuid4())
#         response = self.client.patch(reverse('clientes-detail', args=(self.cliente.uuid,)), {
#             'endereco': endereco
#         })
#         entity = Cliente.objects.get(pk=response.data.get('uuid'))
#         self.assertEqual(endereco, response.data.get('endereco'))
#         self.assertEqual(endereco, str(entity.endereco))
#
#     def test_uudis(self):
#         cliente1 = ClienteFactory(entidade=self.entity)
#         cliente2 = ClienteFactory(entidade=self.entity)
#         ClienteFactory(entidade=self.entity, transiente=True)
#         ClienteFactory.create_batch(3)
#         uuids = '%s,%s' % (cliente1.uuid, cliente2.uuid)
#         response = self.client.get(reverse('clientes-list'), {
#             'uuids': uuids
#         })
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(2, len(response.data))
#         results = response.data
#         self.assertEqual(str(cliente1.uuid), results[0].get('uuid'))
#         self.assertEqual(str(cliente2.uuid), results[1].get('uuid'))
#
#     def test_query(self):
#         cliente = ClienteFactory(nome="Cliente (123)", entidade=self.entity)
#         ClienteFactory(entidade=self.entity, transiente=True)
#         ClienteFactory.create_batch(3)
#         response = self.client.get(reverse('clientes-list'), {
#             'query': '123'
#         })
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(1, len(response.data))
#         results = response.data
#         self.assertEqual(str(cliente.uuid), results[0].get('uuid'))
#         self.assertEqual(str(cliente.nome), results[0].get('nome'))
#
#     def test_post_transiente_true(self):
#         response = self.client.post(reverse('clientes-list'))
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         cliente = Cliente.objects.get(pk=response.data.get('uuid'))
#         self.assertIsNotNone(cliente)
#         self.assertEqual(True, cliente.transiente)
#
#     # def test_post(self):
#     #     response = self.client.post(reverse('clientes-list'), {
#     #         'nome': 'Cliente de teste (post)',
#     #         'telefone_celular': '92832466',
#     #         'endereco': str(uuid.uuid4())
#     #     })
#     #     self.assertEqual(status.HTTP_201_CREATED, response.status_code)
#     #     entity = Cliente.objects.get(pk=response.data.get('uuid'))
#     #     result = response.data
#     #     self.compare_entity(entity, result)
#     #     self.assertEqual(self.entity, entity.entidade)
#     #     self.assertFalse(entity.transiente)
