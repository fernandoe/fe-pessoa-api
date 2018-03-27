# -*- coding:utf-8 -*-
from django.db.models import Q
from rest_framework import status, viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Cliente, Fornecedor
from .serializers import ClienteModelSerializer, FornecedorModelSerializer


class FornecedorCreateAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        entidade = self.request.user.entity
        fornecedor = Fornecedor.objects.create(entidade=entidade)
        return Response({'uuid': fornecedor.uuid}, status=status.HTTP_201_CREATED)


class ClienteCreateAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        entidade = self.request.user.entity
        cliente = Cliente.objects.create(entidade=entidade)
        return Response({'uuid': cliente.uuid}, status=status.HTTP_201_CREATED)


class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = ClienteModelSerializer
    permission_classes = (IsAuthenticated,)

    def filter_queryset(self, queryset):
        filtros = Q()
        if self.action == 'retrieve':
            pass
        elif self.action != 'update':
            filtros = filtros & Q(transiente=False)
        if self.action == 'list':
            uuids = self.request.query_params.get('uuids', None)
            if uuids:
                filtros = filtros & Q(uuid__in=uuids.split(','))
            query = self.request.query_params.get('query', None)
            if query:
                filtros = filtros & Q(nome__icontains=query) | Q(nome_fantasia__icontains=query)
        return queryset.filter(filtros)

    def get_queryset(self):
        return Cliente.objects.filter(entidade=self.request.user.entity)

    def perform_create(self, serializer):
        serializer.save(
            entidade=self.request.user.entity,
            transiente=False
        )

    def perform_update(self, serializer):
        serializer.save(transiente=False)


class FornecedorViewSet(viewsets.ModelViewSet):
    serializer_class = FornecedorModelSerializer
    permission_classes = (IsAuthenticated,)

    def filter_queryset(self, queryset):
        filtros = Q()
        if self.action == 'retrieve':
            pass
        elif self.action != 'update':
            filtros = filtros & Q(transiente=False)
        if self.action == 'list':
            uuids = self.request.query_params.get('uuids', None)
            if uuids:
                filtros = filtros & Q(uuid__in=uuids.split(','))
            query = self.request.query_params.get('query', None)
            if query:
                filtros = filtros & Q(nome__icontains=query) | Q(nome_fantasia__icontains=query)
        return queryset.filter(filtros)

    def get_queryset(self):
        return Fornecedor.objects.filter(entidade=self.request.user.entity)

    def perform_create(self, serializer):
        serializer.save(
            entidade=self.request.user.entity,
            transiente=False
        )

    def perform_update(self, serializer):
        serializer.save(transiente=False)
