from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers

from fe_pessoa.views import ClienteViewSet, FornecedorViewSet, FornecedorCreateAPIView, ClienteCreateAPIView

router = routers.SimpleRouter()
router.register(r'clientes', ClienteViewSet, base_name="clientes")
router.register(r'fornecedores', FornecedorViewSet, base_name="fornecedores")

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'api/v1/fornecedores/novo', FornecedorCreateAPIView.as_view(), name='fornecedores-novo'),
    path(r'api/v1/clientes/novo', ClienteCreateAPIView.as_view(), name='clientes-novo'),
    path(r'api/v1/', include(router.urls)),
    path('version', include('fe_version.urls')),
]
