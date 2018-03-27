from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_jwt.settings import api_settings

from .factories import UserFactory
from ..models import Cliente

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class TestClienteCreateAPIView(APITestCase):

    def setUp(self):
        self.user = UserFactory()
        payload = jwt_payload_handler(self.user)
        token = jwt_encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

    def test_post(self):
        response = self.client.post(reverse('clientes-novo'))
        # print("STATUS CODE: %s - RESPONSE: %s" % (response.status_code, response.content))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(Cliente.objects.get(pk=response.data.get('uuid')))
