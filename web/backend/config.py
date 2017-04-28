from flask import Flask
from flask_socketio import SocketIO


def app_config():
   app = Flask(__name__)
   app.template_folder = '../frontend/templates/'
   app.static_folder = "../frontend/static/"
   app.config['MYSQL_DATABASE_HOST'] = '212.109.220.21'
   app.config['MYSQL_DATABASE_PORT'] = 3406
   app.config['MYSQL_DATABASE_USER'] = 'root'
   app.config['MYSQL_DATABASE_PASSWORD'] = 'SevsL39ZBDzZFdN'
   app.config['MYSQL_DATABASE_DB'] = 'DATAS'
   return app

def my_socket():
    app = app_config()
    socketio = SocketIO(app)
    return socketio
