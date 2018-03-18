# from django.core.cache import cache
# from django.core.urlresolvers import reverse
# from django.test import TestCase
# from rest_framework import status
# from rest_framework.test import APIClient
#
# from fe_core.tests.factories import TokenFactory
# from fe_pessoa.models import Fornecedor
#
#
# class TestFornecedorCreateAPIView(TestCase):
#
#     def setUp(self):
#         self.token = TokenFactory()
#         cache.set(self.token.key, self.token.to_json())
#         self.client = APIClient()
#         self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.token.key))
#
#     def test_post(self):
#         response = self.client.post(reverse('fornecedores-new'))
#         # print "STATUS CODE: %s - RESPONSE: %s" % (response.status_code, response.content)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertIsNotNone(Fornecedor.objects.get(pk=response.data.get('uuid')))
