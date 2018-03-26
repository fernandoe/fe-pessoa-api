from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from .factories import UserFactory
from ..models import Fornecedor





# from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework_jwt.settings import api_settings
#
# from backend.factories import member_factory
#
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER





class TestFornecedorCreateAPIView(APITestCase):

    def setUp(self):
        self.user = UserFactory(email='fer.esp@gmai')
        payload = jwt_payload_handler(self.user)
        token = jwt_encode_handler(payload)
        print('token')
        print(token)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
    #     cache.set(self.token.key, self.token.to_json())
    #     self.client = APIClient()
    #     self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.token.key))

    def test_post(self):
        response = self.client.post(reverse('fornecedores-new'))
        # print "STATUS CODE: %s - RESPONSE: %s" % (response.status_code, response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(Fornecedor.objects.get(pk=response.data.get('uuid')))
