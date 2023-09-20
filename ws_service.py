import ws_models
from utils import validate_registry, validate_hash, generate_token
from spyne import Application, rpc, ServiceBase
from spyne.protocol.soap import Soap11, Soap12
from spyne.server.wsgi import WsgiApplication
from flask import Flask, Response

app = Flask(__name__)

class WSMatriculaOnlineSystem(ServiceBase):
    # pass
    # __tns__ = "http://centralregional/servicos/v1_1"
    @rpc(ws_models.GetMatriculaOnline,
         _no_self=True,
         _body_style="bare",
         _in_message_name="GetMatriculaOnline",
         _out_message_name="GetMatriculaOnlineResponse",
         _returns=ws_models.GetMatriculaOnlineResponse)
    def GetMatriculaOnline(ctx, get_matricula_online):

        try:

            onr_token = saec_api.get_token()
        except Exception as e:
            print(e)
            onr_token = "ERRO"
        
        if validate_hash(get_matricula_online.oRequest.Hash, onr_token):
            try:
                ret = get_registry(get_matricula_online)
            except Exception as e:
                print(e)
                return ws_models.GetMatriculaOnlineResponse(GetMatriculaOnlineResult=ws_models.GetMatriculaOnline_WSResp(Retorno=False, CODIGOERRO=6, Token=generate_token(),
                                                            ERRODESCRICAO="Matrícula indisponível para visualização."))
            print(ret)

            return ret

        return ws_models.GetMatriculaOnlineResponse(
            GetMatriculaOnlineResult=ws_models.GetMatriculaOnline_WSResp(
                Retorno=False, 
                CODIGOERRO=6,
                Token=generate_token(),
                ERRODESCRICAO="Matrícula indisponível para visualização."))

    @rpc(ws_models.ValidaMatriculaOnline,
         _no_self=True,
         _body_style="bare",
         _in_message_name="ValidaMatriculaOnline",
         _out_message_name="ValidaMatriculaOnlineResponse",
         _returns=ws_models.ValidaMatriculaOnlineResponse)
    def ValidaMatriculaOnline(ctx, valida_matricula_online):
        try:
            ret = validate_registry(valida_matricula_online)
        except Exception as e:
            print(e)
            ret = ws_models.ValidaMatriculaOnlineResponse(ValidaMatriculaOnlineResult=ws_models.ValidaMatriculaOnline_WSResp(Retorno=False, CODIGOERRO=4, Token=token,
                                                    ERRODESCRICAO="Matrícula indisponível para visualização."))
        try:
            return ret
        except Exception as e:
            print(e)
            return None


application = Application(
    [WSMatriculaOnlineSystem],
    "http://arisp.tempuri.org/","WSMatriculaOnlineSystemSoap",
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)
wsgi_app = WsgiApplication(application)

