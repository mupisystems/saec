from flask import Flask
from spyne import Application, rpc, ServiceBase
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

app = Flask(__name__)

# Configurações da aplicação Flask
app.config['SECRET_KEY'] = '0ow1gkh+ru*owv6=q%%ffy=b0seri!!skix%_r2=yy8x%=@c2k'

# Importe suas rotas aqui
from app import routes
#from app.ws_service import app as webservice_app

# Importe a instância app do seu web service
import ws_service
app.wsgi_app = ws_service.wsgi_app
