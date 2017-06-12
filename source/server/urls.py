from django.conf.urls import include, url
from rest_framework_nested import routers

from fe_pessoa.views import ClienteViewSet, FornecedorViewSet, ClienteCreateAPIView, FornecedorCreateAPIView


router = routers.SimpleRouter()
router.register(r'clientes', ClienteViewSet, base_name="clientes")
router.register(r'fornecedores', FornecedorViewSet, base_name="fornecedores")

urlpatterns = [
    url(r'^api/v1/clientes/new', ClienteCreateAPIView.as_view(), name='clientes-new'),
    url(r'^api/v1/fornecedores/new', FornecedorCreateAPIView.as_view(), name='fornecedores-new'),
    url(r'^api/v1/', include(router.urls)),
]
