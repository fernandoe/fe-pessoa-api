# # -*- coding:utf-8 -*-
# import logging
#
# from django.conf import settings
#
# from usuario.models import Usuario
# from pessoa.models import Telefone, Email, Endereco, PessoaUsuario
#
#
# logger = logging.getLogger(settings.APP_LOOGER)
#
#
# def get_usuarios_ids(request, empresa):
#     usuariosUUID = request.getlist('usuarios')
#     usuariosIDs = []
#     for usuarioUUID in usuariosUUID:
#         uId = Usuario.objects.get(uuid=usuarioUUID, empresa=empresa).id
#         usuariosIDs.append(uId)
#     return usuariosIDs
#
#
# def salvar_usuarios(pessoa, request, _pessoa):
#         usuarios_uuid = request.POST.getlist('usuarios', None)
#         if usuarios_uuid:
#             p = _pessoa.objects.get(uuid=pessoa.uuid)
#             pd_delete = PessoaUsuario.objects.filter(pessoa=p, empresa = request.user.empresa).exclude(usuario__uuid__in=usuarios_uuid)
#             pd_delete.delete()
#             for u_uuid in usuarios_uuid:
#                 usuario = Usuario.objects.get(uuid=u_uuid)
#                 try:
#                     PessoaUsuario.objects.get(
#                         pessoa  = p,
#                         usuario = usuario,
#                         empresa = request.user.empresa
#                     )
#                 except PessoaUsuario.DoesNotExist:
#                     PessoaUsuario.objects.create(
#                         pessoa  = p,
#                         usuario = usuario,
#                         empresa = request.user.empresa
#                     )
#
# def salvar_telefones(pessoa, request):
#         # TELEFONE CELULAR
#         celular_uuid = request.POST.get('celular_uuid', None)
#         celular      = request.POST.get('celular', None)
#         if celular_uuid:
#             telefone_celular = pessoa.telefone_set.get(uuid=celular_uuid)
#             if celular:
#                 telefone_celular.tipo     = Telefone.TELEFONE_TIPO_CELULAR
#                 telefone_celular.telefone = celular
#                 telefone_celular.save()
#             else:
#                 telefone_celular.delete()
#         else:
#             if celular:
#                 telefone_celular    = Telefone(
#                         tipo     = Telefone.TELEFONE_TIPO_CELULAR,
#                         telefone = celular,
#                     )
#                 pessoa.telefone_set.add(telefone_celular)
#         # TELEFONE COMERCIAL
#         comercial_uuid = request.POST.get('comercial_uuid', None)
#         comercial      = request.POST.get('comercial', None)
#         if comercial_uuid:
#             telefone_comercial = pessoa.telefone_set.get(uuid=comercial_uuid)
#             if comercial:
#                 telefone_comercial.tipo     = Telefone.TELEFONE_TIPO_COMERCIAL
#                 telefone_comercial.telefone = comercial
#                 telefone_comercial.save()
#             else:
#                 telefone_comercial.delete()
#         else:
#             if comercial:
#                 telefone_comercial = Telefone(
#                         tipo     = Telefone.TELEFONE_TIPO_COMERCIAL,
#                         telefone = comercial,
#                     )
#                 pessoa.telefone_set.add(telefone_comercial)
#         # TELEFONE RESIDENCIAL
#         residencial_uuid = request.POST.get('residencial_uuid', None)
#         residencial      = request.POST.get('residencial', None)
#         if residencial_uuid:
#             telefone_residencial = pessoa.telefone_set.get(uuid=residencial_uuid)
#             if residencial:
#                 telefone_residencial.tipo       = Telefone.TELEFONE_TIPO_RESIDENCIAL
#                 telefone_residencial.telefone   = residencial
#                 telefone_residencial.save()
#             else:
#                 telefone_residencial.delete()
#         else:
#             if residencial:
#                 telefone_residencial = Telefone(
#                         tipo     = Telefone.TELEFONE_TIPO_RESIDENCIAL,
#                         telefone = residencial,
#                     )
#                 pessoa.telefone_set.add(telefone_residencial)
#
#
# def salvar_emails(pessoa, request):
#     # EMAIL PESSOAL
#     e_pessoal_uuid = request.POST.get('e_pessoal_uuid', None)
#     e_pessoal      = request.POST.get('e_pessoal', None)
#     if e_pessoal_uuid:
#         email_pessoal = pessoa.email_set.get(uuid=e_pessoal_uuid)
#         if e_pessoal:
#             email_pessoal.tipo  = Email.EMAIL_TIPO_PESSOAL
#             email_pessoal.email = e_pessoal
#             email_pessoal.save()
#         else:
#             email_pessoal.delete()
#     else:
#         if e_pessoal:
#             email_pessoal = Email(
#                     tipo  = Email.EMAIL_TIPO_PESSOAL,
#                     email = e_pessoal,
#                 )
#             pessoa.email_set.add(email_pessoal)
#     # EMAIL COMERCIAL
#     e_comercial_uuid = request.POST.get('e_comercial_uuid', None)
#     e_comercial      = request.POST.get('e_comercial', None)
#     if e_comercial_uuid:
#         email_comercial = pessoa.email_set.get(uuid=e_comercial_uuid)
#         if e_comercial:
#             email_comercial.tipo  = Email.EMAIL_TIPO_COMERCIAL
#             email_comercial.email = e_comercial
#             email_comercial.save()
#         else:
#             email_comercial.delete()
#     else:
#         if e_comercial:
#             email_comercial = Email(
#                     tipo  = Email.EMAIL_TIPO_COMERCIAL,
#                     email = e_comercial,
#                 )
#             pessoa.email_set.add(email_comercial)
#
#
# def salvar_enderecos(pessoa, tipo, request):
#     if tipo == 'F':
#         endereco1_uuid = request.POST.get('endereco1_uuid', None)
#         cep1           = request.POST.get('cep1', None)
#         logradouro1    = request.POST.get('logradouro1', None)
#         numero1        = request.POST.get('numero1', None)
#         complemento1   = request.POST.get('complemento1', None)
#         bairro1        = request.POST.get('bairro1', None)
#         cidade1        = request.POST.get('cidade1', None)
#         estado1        = request.POST.get('estado1', None)
#
#         if endereco1_uuid:
#             e1 = pessoa.endereco_set.get(uuid=endereco1_uuid)
#             e1.tipo        = Endereco.ENDERECO_TIPO_RESIDENCIAL
#             e1.logradouro  = logradouro1
#             e1.numero      = numero1
#             e1.complemento = complemento1
#             e1.bairro      = bairro1
#             e1.cidade      = cidade1
#             e1.estado      = estado1
#             e1.cep         = cep1
#             e1.save()
#         else:
#             e1 = Endereco(
#                 tipo        = Endereco.ENDERECO_TIPO_RESIDENCIAL,
#                 logradouro  = logradouro1,
#                 numero      = numero1,
#                 complemento = complemento1,
#                 bairro      = bairro1,
#                 cidade      = cidade1,
#                 estado      = estado1,
#                 cep         = cep1
#             )
#             pessoa.endereco_set.add(e1)
#     if tipo == 'F' or tipo == 'J':
#         endereco2_uuid = request.POST.get('endereco2_uuid', None)
#         cep2           = request.POST.get('cep2', None)
#         logradouro2    = request.POST.get('logradouro2', None)
#         numero2        = request.POST.get('numero2', None)
#         complemento2   = request.POST.get('complemento2', None)
#         bairro2        = request.POST.get('bairro2', None)
#         cidade2        = request.POST.get('cidade2', None)
#         estado2        = request.POST.get('estado2', None)
#         if endereco2_uuid:
#             e2 = pessoa.endereco_set.get(uuid=endereco2_uuid)
#             e2.tipo        = Endereco.ENDERECO_TIPO_COMERCIAL
#             e2.logradouro  = logradouro2
#             e2.numero      = numero2
#             e2.complemento = complemento2
#             e2.bairro      = bairro2
#             e2.cidade      = cidade2
#             e2.estado      = estado2
#             e2.cep         = cep2
#             e2.save()
#         else:
#             e2 = Endereco(
#                 tipo        = Endereco.ENDERECO_TIPO_COMERCIAL,
#                 logradouro  = logradouro2,
#                 numero      = numero2,
#                 complemento = complemento2,
#                 bairro      = bairro2,
#                 cidade      = cidade2,
#                 estado      = estado2,
#                 cep         = cep2
#             )
#             pessoa.endereco_set.add(e2)
# #    if tipo == 'J':
# #        endereco2_uuid = request.POST.get('endereco2_uuid', None)
# #        cep2           = request.POST.get('cep2', None)
# #        logradouro2    = request.POST.get('logradouro2', None)
# #        numero2        = request.POST.get('numero2', None)
# #        complemento2   = request.POST.get('complemento2', None)
# #        bairro2        = request.POST.get('bairro2', None)
# #        cidade2        = request.POST.get('cidade2', None)
# #        estado2        = request.POST.get('estado2', None)
# #        if endereco2_uuid:
# #            e2 = pessoa.endereco_set.get(uuid=endereco2_uuid)
# #            e2.tipo        = Endereco.ENDERECO_TIPO_COMERCIAL
# #            e2.logradouro  = logradouro2
# #            e2.numero      = numero2
# #            e2.complemento = complemento2
# #            e2.bairro      = bairro2
# #            e2.cidade      = cidade2
# #            e2.estado      = estado2
# #            e2.cep         = cep2
# #            e2.save()
# #        else:
# #            e2 = Endereco(
# #                tipo        = Endereco.ENDERECO_TIPO_RESIDENCIAL,
# #                logradouro  = logradouro2,
# #                numero      = numero2,
# #                complemento = complemento2,
# #                bairro      = bairro2,
# #                cidade      = cidade2,
# #                estado      = estado2,
# #                cep         = cep2
# #            )
# #            pessoa.endereco_set.add(e2)