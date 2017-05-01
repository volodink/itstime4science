from flask import Flask, render_template
from flask.ext.mysql import MySQL
import sys
import os
import parsing
import content
import math
from flask_socketio import SocketIO
from flask_socketio import send, emit
import json

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
@app.route("/")
def main():
    return render_template('index.html', is_dev=is_dev, data = data["main"], main = True)

@app.route("/copter")
def copter():
    return render_template('index.html', is_dev=is_dev, data = data["copter"])

@app.route("/satellite")
def satellite():
    return render_template('index.html', is_dev=is_dev, data = data["satellite"])

@app.route("/mcc")
def mcc():
    return render_template('mcc.html', is_dev=is_dev)

@socketio.on('connect', namespace='/mcc')
def ws_conn():
    json_data = parsing.getData(mysql)
    socketio.emit('packet', {'json_data': json_data}, namespace='/mcc')

if __name__ == '__main__':
    mysql.init_app(app)
socketio.run(app,host="0.0.0.0", debug=True)