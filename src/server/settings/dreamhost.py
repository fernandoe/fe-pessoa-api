from .base import *
import os
from configparser import RawConfigParser

config = RawConfigParser()
config.read(os.environ.get('CONFIGURATIONS_FILE'))

ALLOWED_HOSTS = ['*']

# OAUTH2_PROVIDER = {
#     'RESOURCE_SERVER_INTROSPECTION_URL': config.get('common', 'INTROSPECT_URL'),
#     'RESOURCE_SERVER_AUTH_TOKEN': config.get('common', 'INTROSPECT_TOKEN'),
#     'OAUTH2_VALIDATOR_CLASS': 'fe_core.services.auth.oauth2_validators.FEOAuth2Validator'
# }

STATIC_ROOT = config.get('fe-pessoa-server', 'STATIC_ROOT')
