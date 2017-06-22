from django.core.urlresolvers import reverse
from django.test import TestCase
from fe_core.tests.factories import AccessTokenFactory
from rest_framework import status
from rest_framework.test import APIClient

from fe_pessoa.models import Cliente


class TestClienteCreateAPIView(TestCase):

    def setUp(self):
        self.token = AccessTokenFactory().token
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_post(self):
        response = self.client.post(reverse('clientes-new'))
        # print "STATUS CODE: %s - RESPONSE: %s" % (response.status_code, response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(Cliente.objects.get(pk=response.data.get('uuid')))
