# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-12 01:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('transiente', models.BooleanField(default=True, editable=False)),
                ('entidade', models.UUIDField()),
                ('nome', models.CharField(max_length=128, null=True)),
                ('cpf', models.CharField(blank=True, max_length=14, null=True)),
                ('nome_fantasia', models.CharField(blank=True, max_length=128, null=True)),
                ('contato', models.CharField(blank=True, max_length=128, null=True)),
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('inscricao_estadual', models.CharField(blank=True, max_length=20, null=True)),
                ('inscricao_municipal', models.CharField(blank=True, max_length=20, null=True)),
                ('endereco', models.UUIDField(blank=True, null=True)),
                ('telefone_celular', models.CharField(blank=True, max_length=32, null=True)),
                ('telefone_comercial', models.CharField(blank=True, max_length=32, null=True)),
                ('telefone_residencial', models.CharField(blank=True, max_length=32, null=True)),
                ('telefone_recado', models.CharField(blank=True, max_length=32, null=True)),
                ('site', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('observacao', models.TextField(blank=True, null=True)),
                ('ativo', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('nome',),
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fe_pessoa.Pessoa')),
            ],
            options={
                'ordering': ('nome',),
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
            bases=('fe_pessoa.pessoa',),
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fe_pessoa.Pessoa')),
            ],
            options={
                'ordering': ('nome',),
                'verbose_name': 'Fornecedor',
                'verbose_name_plural': 'Fornecedores',
            },
            bases=('fe_pessoa.pessoa',),
        ),
    ]