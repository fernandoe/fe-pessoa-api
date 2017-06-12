# import uuid
#
# from django.core.cache import cache
# from django.core.urlresolvers import reverse
# from django.test import TestCase
# from rest_framework import status
# from rest_framework.test import APIClient
#
# from fe_core.tests.factories import TokenFactory
# from fe_pessoa.models import Fornecedor
# from fe_pessoa.tests.factories import FornecedorFactory
#
#
# class TestFornecedorViewSet(TestCase):
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
#         self.fornecedor = FornecedorFactory(entidade=self.entidade)
#
#     def test_get(self):
#         response = self.client.get(reverse('fornecedores-list'))
#         # print "STATUS CODE: %s - RESPONSE: %s" % (response.status_code, response.content)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(1, response.data.get('count'))
#
#     def test_get_transiente_true(self):
#         fornecedor = FornecedorFactory(entidade=self.entidade, transiente=True)
#         response = self.client.get(reverse('fornecedores-detail', args=(fornecedor.uuid,)))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         # print "STATUS CODE: %s - RESPONSE: %s" % (response.status_code, response.content)
#         self.assertEqual(str(fornecedor.uuid), response.data.get('uuid'))
#         self.assertTrue(fornecedor.transiente)
#
#     def test_get_transiente_false(self):
#         fornecedor = FornecedorFactory(entidade=self.entidade, transiente=False)
#         response = self.client.get(reverse('fornecedores-detail', args=(fornecedor.uuid,)))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         # print "STATUS CODE: %s - RESPONSE: %s" % (response.status_code, response.content)
#         self.assertEqual(str(fornecedor.uuid), response.data.get('uuid'))
#         self.assertFalse(fornecedor.transiente)
#
#     def test_post(self):
#         response = self.client.post(reverse('fornecedores-list'), {
#             'nome': 'Fornecedor de teste (post)',
#             'telefone_celular': '92832466',
#             'endereco': str(uuid.uuid4())
#         })
#         # print "STATUS CODE: %s - RESPONSE: %s" % (response.status_code, response.content)
#         self.assertEqual(status.HTTP_201_CREATED, response.status_code)
#         entity = Fornecedor.objects.get(pk=response.data.get('uuid'))
#         result = response.data
#         self.compare_entity(entity, result)
#         self.assertEqual(self.entidade, str(entity.entidade))
#         self.assertFalse(entity.transiente)
#
#     def test_put(self):
#         fornecedor = Fornecedor.objects.create(entidade=self.entidade)
#         self.assertTrue(fornecedor.transiente)
#         response = self.client.put(reverse('fornecedores-detail', args=(fornecedor.uuid,)), {
#             'nome': 'Fornecedor de teste (put)',
#             'telefone_celular': '92832466',
#             'endereco': str(uuid.uuid4())
#         })
#         # print "STATUS CODE: %s - RESPONSE: %s" % (response.status_code, response.content)
#         self.assertEqual(status.HTTP_200_OK, response.status_code)
#         entity = Fornecedor.objects.get(pk=response.data.get('uuid'))
#         result = response.data
#         self.compare_entity(entity, result)
#         self.assertEqual(self.entidade, str(entity.entidade))
#         self.assertFalse(entity.transiente)
#
#     def test_patch_endereco(self):
#         endereco = str(uuid.uuid4())
#         response = self.client.patch(reverse('fornecedores-detail', args=(self.fornecedor.uuid,)), {
#             'endereco': endereco
#         })
#         # print "STATUS CODE: %s - RESPONSE: %s" % (response.status_code, response.content)
#         entity = Fornecedor.objects.get(pk=response.data.get('uuid'))
#         self.assertEqual(endereco, response.data.get('endereco'))
#         self.assertEqual(endereco, str(entity.endereco))
#
#     def test_uudis(self):
#         fornecedor1 = FornecedorFactory(entidade=self.entidade)
#         fornecedor2 = FornecedorFactory(entidade=self.entidade)
#         FornecedorFactory(entidade=self.entidade, transiente=True)
#         FornecedorFactory.create_batch(3)
#         uuids = '%s,%s' % (fornecedor1.uuid, fornecedor2.uuid)
#         response = self.client.get(reverse('fornecedores-list'), {
#             'uuids': uuids
#         })
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         # print "STATUS CODE: %s - RESPONSE: %s" % (response.status_code, response.content)
#         self.assertEqual(2, response.data.get('count'))
#         results = response.data.get('results')
#         self.assertEqual(str(fornecedor1.uuid), results[0].get('uuid'))
#         self.assertEqual(str(fornecedor2.uuid), results[1].get('uuid'))
#
#     def test_query(self):
#         fornecedor = FornecedorFactory(nome="Fornecedor (123)", entidade=self.entidade)
#         FornecedorFactory(entidade=self.entidade, transiente=True)
#         FornecedorFactory.create_batch(3)
#         response = self.client.get(reverse('fornecedores-list'), {
#             'query': '123'
#         })
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         # print "STATUS CODE: %s - RESPONSE: %s" % (response.status_code, response.content)
#         self.assertEqual(1, response.data.get('count'))
#         results = response.data.get('results')
#         self.assertEqual(str(fornecedor.uuid), results[0].get('uuid'))
#         self.assertEqual(str(fornecedor.nome), results[0].get('nome'))
