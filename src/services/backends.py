import requests
from django.contrib.auth import get_user_model
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication, get_authorization_header
from rest_framework_jwt.settings import api_settings

jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
User = get_user_model()


class FEMicroservicesBackend(BaseAuthentication):
    def authenticate(self, request, token=None):
        auth = get_authorization_header(request).split()
        if auth and auth[0].lower() == b'bearer':

            if len(auth) == 1:
                msg = 'Invalid token header. No credentials provided.'
                raise exceptions.AuthenticationFailed(msg)
            elif len(auth) > 2:
                msg = 'Invalid token header. Token string should not contain spaces.'
                raise exceptions.AuthenticationFailed(msg)

            try:
                token = auth[1].decode()
                response = requests.post('http://conta:8000/verify/', data={
                    'token': token
                })
                if response.status_code == 400:
                    print(response.content)
                    raise exceptions.AuthenticationFailed('Invalid credentials')

                info = jwt_decode_handler(token)
                try:
                    user = User.objects.get(pk=info['user_id'])
                except User.DoesNotExist:
                    user = User.objects.create(
                        pk=info['user_id'],
                        email=info['email']
                    )
                return user, token
            except UnicodeError:
                msg = 'Invalid token header. Token string should not contain invalid characters.'
                raise exceptions.AuthenticationFailed(msg)
        else:
            return None


class FEMicroservicesBackendTesting(BaseAuthentication):
    def authenticate(self, request, token=None):
        auth = get_authorization_header(request).split()
        if auth and auth[0].lower() == b'bearer':

            if len(auth) == 1:
                msg = 'Invalid token header. No credentials provided.'
                raise exceptions.AuthenticationFailed(msg)
            elif len(auth) > 2:
                msg = 'Invalid token header. Token string should not contain spaces.'
                raise exceptions.AuthenticationFailed(msg)

            try:
                token = auth[1].decode()
                info = jwt_decode_handler(token)
                try:
                    user = User.objects.get(pk=info['user_id'])
                except User.DoesNotExist:
                    user = User.objects.create(
                        pk=info['user_id'],
                        email=info['email']
                    )
                return user, token
            except UnicodeError:
                msg = 'Invalid token header. Token string should not contain invalid characters.'
                raise exceptions.AuthenticationFailed(msg)
        else:
            return None
