from flask import Flask, render_template
from flask.ext.mysql import MySQL
import sys
import os
import parsing
import content
import urllib.request

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

@socketio.on('my_event', namespace='/mcc')
def message(message):
        json_data = parsing.getData(mysql)
        mas = json.loads(json_data)
        if message['data'] != mas[0]['id']:
            emit('packet', {'json_data': json_data}, namespace='/mcc')
        else:
            emit('packet', {'json_data': 0}, namespace='/mcc')

@socketio.on('my_event2', namespace='/mcc')
def message():
    needeble_erl='https://api.aprs.fi/api/get?name=UB4FEU-11&what=loc&apikey=APIKEY&format=json'
    response = urllib.request.urlopen(needeble_erl)

@socketio.on('last_dots', namespace='/mcc')
def msg():
    i=10
    json_data = parsing.last_dots(mysql,i)
    emit('lastMarkers', {'json_data': json_data}, namespace='/mcc')


if __name__ == '__main__':
    mysql.init_app(app)
    if is_dev == 1:
        socketio.run(app, host='0.0.0.0', debug=True)
    else:
        socketio.run(app, host='0.0.0.0',)
