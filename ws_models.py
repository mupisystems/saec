import decimal

from spyne import Integer, Unicode
from spyne.model.complex import ComplexModel, Array, XmlData
from spyne.model.primitive.string import String
from spyne.model.primitive import Date, Boolean, DateTime
from spyne.model.enum import Enum
from spyne.model.binary import ByteArray
from spyne import Unicode, Iterable, XmlAttribute
from spyne.model.complex import Iterable, XmlAttribute, ComplexModel, ComplexModelMeta, ComplexModelBase

class DefaultModel(ComplexModel):
    __namespace__ = "http://arisp.tempuri.org/"

class IntType(Integer):
    __type_name__ = 'int'

class MatriculaOnlineRequest(DefaultModel):

    _type_info = [
        ("identificacao", Unicode),
        ("cartorio", Unicode),
        ("solicitante", Unicode),
        ("itens", Unicode)
    ]

class ValidaMatriculaOnline_WSReq(DefaultModel):
    _type_info = [
        ("Matricula", Unicode(nillable=False)),
    ]


class GetMatriculaOnline_WSReq(DefaultModel):
    _type_info = [
        ("Hash", Unicode(nillable=False,min_occurs=0,max_occurs=1)),
        ("Matricula", Unicode(nillable=False,min_occurs=0,max_occurs=1)),
        ("IDPedido", IntType(nillable=False,min_occurs=1,max_occurs=1))
    ]


class oRequestHash(DefaultModel):
    _type_info = [
        ("Hash", Unicode),
    ]


class ValidaMatriculaOnline(DefaultModel):

    _type_info = [
        ("oRequest", ValidaMatriculaOnline_WSReq),
    ]


class GetToken(DefaultModel):

    _type_info = [
        ("oRequest", oRequestHash),
    ]


class GetMatriculaOnline(DefaultModel):

    _type_info = [
        ("oRequest", GetMatriculaOnline_WSReq),
    ]


class GetMatriculaOnline_WSResp(DefaultModel):

    _type_info = [
        ('Retorno', Boolean(nillable=False,min_occurs=1,max_occurs=1)),
        ('Token', Unicode(nillable=False,min_occurs=0,max_occurs=1)),
        ('QtdeImagens', IntType(nillable=False,min_occurs=1,max_occurs=1)),
        #('TipoImagem', Unicode(values=["TIFF", "GIF", "JPG", "PNG"],nillable=False,min_occurs=1,max_occurs=1,
        #    type_name='EnumTipoImagem')),
        ('TipoImagem ',Enum("TIFF", "GIF", "JPG", "PNG",type_name='EnumTipoImagem')),
        ('URLImagens', Unicode(nillable=False,min_occurs=0,max_occurs=1)),
        ('CODIGOERRO', IntType(nillable=False,min_occurs=1,max_occurs=1)),
        ('ERRODESCRICAO', Unicode(nillable=False,min_occurs=1,max_occurs=1)),
    ]

class GetMatriculaOnlineResponse(DefaultModel):

    _type_info = [
        ('GetMatriculaOnlineResult', GetMatriculaOnline_WSResp),
    ]



class GetTokenResult(DefaultModel):

    _type_info = [
        ('Retorno', Boolean),
        ('Token', Unicode(nillable=False)),
        ('CODIGOERRO', IntType(nillable=False)),
        ('ERRODESCRICAO', Unicode(nillable=False)),
    ]


class ValidaMatriculaOnline_WSResp(DefaultModel):

    _type_info = [
        ('Retorno', Boolean(nillable=False,min_occurs=1,max_occurs=1)),
        ('DataRegistro', DateTime(nillable=False,min_occurs=1,max_occurs=1)),
        ('CODIGOERRO', IntType(nillable=False,min_occurs=1,max_occurs=1)),
        ('ERRODESCRICAO', Unicode(nillable=False,min_occurs=0,max_occurs=1)),
    ]
    __type_max_occurs__=1


class ValidaMatriculaOnlineResponse(DefaultModel):

    _type_info = [
        ('ValidaMatriculaOnlineResult', ValidaMatriculaOnline_WSResp),
    ]
    __type_max_occurs__=1
    __type_min_occurs__=0

class Status(DefaultModel):
    _type_info = [
        ('Codigo', IntType),
        ('Erro', Unicode)
    ]

class NMatString(Integer):
    __type_name__ = 'int'

class Ocorrencia(DefaultModel):
    _type_info = [
        ('Qtde', IntType),
        ('NMatriculas', Array(NMatString, min_occurs=1,
                               nillable=True, type_name='ArrayOfInt'))
    ]

    class Attributes(DefaultModel.Attributes):
        max_occurs = decimal.Decimal("inf")


class Cartorio(DefaultModel):
    _type_info = [
        ('Identificacao', Unicode),
        ('NomeUsuarioPesquisado', Unicode),
        ('CPFCNPJ', Unicode),
        ('Ocorrencias', Ocorrencia),
        ('Status', Status),
    ]

    class Attributes(DefaultModel.Attributes):
        max_occurs = decimal.Decimal("inf")


class Cartorios(DefaultModel):
    _type_info = [
        ('Cartorio', Cartorio)
    ]



class GetOccurrences(DefaultModel):

    _type_info = [
        ('cpfCnpj', Unicode),
        ('validationHash', Unicode),
    ]


class GetOccurrencesResult(DefaultModel):

    _type_info = [
        ('Cartorios', Cartorios),
    ]

class GetOccurrencesResponse(DefaultModel):

    _type_info = [
        ('GetOccurrencesResult', GetOccurrencesResult),
    ]