import os
import os
import sys
import urllib.request

from flask import Flask
from flask.ext.mysql import MySQL
from flask_socketio import SocketIO
from flask_socketio import emit

import content
import parsing

app = Flask(__name__)

app.config['MYSQL_DATABASE_HOST'] = os.getenv("MYSQL_DATABASE_HOST", "0")
app.config['MYSQL_DATABASE_PORT'] = int(os.getenv("MYSQL_DATABASE_PORT", "0"))
app.config['MYSQL_DATABASE_USER'] = os.getenv("MYSQL_DATABASE_USER", "0")
app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv("MYSQL_DATABASE_PASSWORD", "0")
app.config['MYSQL_DATABASE_DB'] = os.getenv("MYSQL_DATABASE_DB", "0")

app.template_folder = '../frontend/templates/'
app.static_folder = "../frontend/static/"


socketio = SocketIO(app)

mysql = MySQL(app)

is_dev = int(os.getenv("DEV", "0"))
sys.path.append(str(os.path.abspath(sys.argv[0])))

data = content.getContent()

from modules.flask_routes import *
from modules.socketio_routes import *

if __name__ == '__main__':
    mysql.init_app(app)
    if is_dev == 1:
        socketio.run(app, host='0.0.0.0', debug=True)
    else:
        socketio.run(app, host='0.0.0.0')