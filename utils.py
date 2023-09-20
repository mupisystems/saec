import ws_models
from datetime import date, datetime, time
from secrets import token_urlsafe

def validate_hash(incoming_hash, onr_token):
    '''
    validar hash recebido na solicitação
    '''

    return True

def generate_token():
    return token_urlsafe(16)

def validate_registry(item):
    '''
    essa função precisa fazer algum tipo de consulta em banco de dados para validar se o número de matrícula
    solicitado existe
    '''

    #gerar exemplo com número de matrícula de 1 a 100
    lista_matriculas = []
    for i in range(0,100):
        lista_matriculas.append({'matricula':i,'data_registro':date(2022,1,10)})


    matricula = next((item for item in lista_matriculas if item['matricula'] == item.oRequest.Matricula), None)

    if not matricula:
        return ws_models.ValidaMatriculaOnlineResponse(
            ValidaMatriculaOnlineResult=ws_models.ValidaMatriculaOnline_WSResp(
                Retorno=False, 
                CODIGOERRO=4,
                ERRODESCRICAO="Matrícula indisponível para visualização."
                )
            )

    date_registry = datetime.combine(registry.date_registry,time(18,0))

    return ws_models.ValidaMatriculaOnlineResponse(
        ValidaMatriculaOnlineResult=spyne_model.ValidaMatriculaOnline_WSResp(
            Retorno=True,
            DataRegistro=datetime.combine(matricula.get('data_registro'),time(18,0)),
            CODIGOERRO=0,
            ERRODESCRICAO=""))
