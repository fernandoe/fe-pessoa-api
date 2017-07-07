from .base import *

ALLOWED_HOSTS = ['*']

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.authentication.OAuth2Authentication',
    )
}

AUTHENTICATION_BACKENDS = (
    'oauth2_provider.backends.OAuth2Backend',
    'django.contrib.auth.backends.ModelBackend'
)

OAUTH2_PROVIDER = {
    'RESOURCE_SERVER_INTROSPECTION_URL': 'https://auth.fe.fernandoe.com/api/v1/introspect/',
    'RESOURCE_SERVER_AUTH_TOKEN': 'fe-pessoa-server',
    'OAUTH2_VALIDATOR_CLASS': 'fe_core.services.auth.oauth2_validators.FEOAuth2Validator'
}

STATIC_ROOT = '/home/fems/pessoa.fe.fernandoe.com/public/static'
