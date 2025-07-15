from asgiref.wsgi import WsgiToAsgi
from app.app import app as flask_app

app = WsgiToAsgi(flask_app)
