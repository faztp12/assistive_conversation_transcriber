from flask import Flask, session
from flask_session import Session
from flask_socketio import SocketIO
import os
dev_port = (os.environ['DEV_PORT']) or 3000
if isinstance(dev_port, str):
  dev_port = int(dev_port)

app = Flask(__name__)
Session(app)
socketio = SocketIO(app)

from .controllers.auth import init_app as init_auth_routes
init_auth_routes(app)

from .controllers.transcription import init_app as init_trans_routes
init_trans_routes(app, session, socketio)

def start_dev_server():
  socketio.run(app, port=dev_port, host="0.0.0.0", debug=True)
