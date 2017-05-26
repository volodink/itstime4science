from flask import Flask,request, render_template
from flask.ext.mysql import MySQL
import sys
import os
from modules import parsing
from modules import reports
from modules import content
from flask_socketio import SocketIO
from flask_socketio import send, emit
import json
import html
import urllib.request
#import decode_aprs

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
    return render_template('mcc.html', is_dev=is_dev, panel_tags=content.panel_tags, communication_channel_panel=content.communication_channel_panel)
@app.route("/telemetriya",methods=['GET'])
def telem():
    return parsing.pasing_telem(mysql)


@socketio.on('my_event', namespace='/mcc')
def message(message):
        json_data = parsing.getData(mysql)
        mas = json.loads(json_data)
        if message['data'] != mas[0]['id']:
            emit('gprs', {'json_data': json_data,'type': 'gprs'}, namespace='/mcc')
        else:
            emit('gprs', {'json_data': 0,'type': 'gprs'}, namespace='/mcc')

#@socketio.on('my_event2', namespace='/mcc')
#def message():
#    response = urllib.request.urlopen('https://api.aprs.fi/api/get?name=UB4FEU-11&what=loc&apikey=96108.wFh6EKTmYPxnt&format=json')
#     print(response.read())
#    decode_aprs(response)
#    emit('aprs', {'response': response}, namespace='/mcc')


@socketio.on('last_dots', namespace='/mcc')
def msg():
    json_data = parsing.last_dots(mysql)
    emit('lastMarkers', {'json_data': json_data, 'type': 'gprs'}, namespace='/mcc')

@socketio.on('report', namespace='/mcc')
def msg():
    json_data = parsing.last_dots(mysql)
    emit('lastMarkers', {'json_data': json_data, 'type': 'gprs'}, namespace='/mcc')


if __name__ == '__main__':
    mysql.init_app(app)
    reports.report(mysql)
    if is_dev == 1:
        socketio.run(app, host='0.0.0.0', debug=True)
    else:
        socketio.run(app, host='0.0.0.0')