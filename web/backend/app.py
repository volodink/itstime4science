from flask import Flask,request, render_template, send_from_directory
from flask.ext.mysql import MySQL
import sys
import os
from modules import parsing
from modules import content
from modules import report_json
from flask_socketio import SocketIO
from flask_socketio import send, emit
import json
import aprslib

import urllib.request
from modules import create_report
from modules import archivator
from subprocess import Popen, PIPE

app = Flask(__name__)
app.config['MYSQL_DATABASE_HOST'] = os.getenv("MYSQL_DATABASE_HOST", "0")
app.config['MYSQL_DATABASE_PORT'] = int(os.getenv("MYSQL_DATABASE_PORT", "0"))
app.config['MYSQL_DATABASE_USER'] = os.getenv("MYSQL_DATABASE_USER", "0")
app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv("MYSQL_DATABASE_PASSWORD", "0")
app.config['MYSQL_DATABASE_DB'] = os.getenv("MYSQL_DATABASE_DB", "0")



app.template_folder = '../frontend/templates/'
app.static_folder = '../frontend/static/'


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

@app.route("/report")
def report():
    return render_template('report.html', is_dev=is_dev)


@app.route("/telemetry",methods=['GET'])
def telem():
    return parsing.parsing_telem(mysql)


@app.route('/rep')
def download():
    try:
        if (g != l_g) and (a !=l_a) and (t!=l_t):
            g,a,t = create_report.getData(mysql)
            l_g,l_a,l_t = g,a,t
            archivator.img_zip()
            return send_from_directory('modules/', 'report.zip')
        else:
            return send_from_directory('modules/', 'report.zip')
    except:
        g,a,t = create_report.getData(mysql)
        global g,a,t,l_g,l_a,l_t
        l_g,l_a,l_t = g,a,t
        archivator.img_zip()
        return send_from_directory('modules/', 'report.zip')


@socketio.on('event_report', namespace='/report')
def rep():
    json_gprs = report_json.gprs(mysql)
    json_aprs = report_json.aprs(mysql)
    json_telemetry = report_json.telemetry(mysql)

    emit('json_report', {'json_gprs': json_gprs,'json_aprs': json_aprs,'json_telemetry': json_telemetry}, namespace='/report')



@socketio.on('my_event', namespace='/mcc')
def message(message):
    try:
        json_data = parsing.pars_gprs(mysql)
        mas = json.loads(json_data)
        if message['data'] != mas[0]['id']:
            emit('gprs', {'json_data': json_data,'type': 'gprs'}, namespace='/mcc')
        else:
            emit('gprs', {'json_data': 0,'type': 'gprs'}, namespace='/mcc')
    except:
        emit('gprs', {'json_data': 0,'type': 'gprs'}, namespace='/mcc')
@socketio.on('my_event2', namespace='/mcc')
def message(message):
    try:
        json_data = parsing.pars_aprs(mysql)
        mas = json.loads(json_data)
        if message['data'] != mas[0]['id']:
            emit('aprs', {'json_data': json_data, 'type': 'aprs'}, namespace='/mcc')    
        else:
            emit('aprs', {'json_data': 0, 'type': 'aprs'}, namespace='/mcc')
    except:
        emit('aprs', {'json_data': 0, 'type': 'aprs'}, namespace='/mcc')
@socketio.on('my_event3', namespace='/mcc')
def message(message):
    try:
        json_data = parsing.pars_telemetry(mysql)
        mas = json.loads(json_data)
        if message['data'] != mas[0]['id']:       
            emit('telemetry', {'json_data': json_data, 'type': 'telemetry'}, namespace='/mcc')
        else:
            emit('telemetry', {'json_data': 0, 'type': 'telemetry'}, namespace='/mcc')
    except:
        emit('telemetry', {'json_data': 0, 'type': 'telemetry'}, namespace='/mcc')
@socketio.on('last_dots', namespace='/mcc')
def msg():
    gprs = parsing.last_gprs_dots(mysql)
    aprs = parsing.last_aprs_dots(mysql)
    telemetry = parsing.last_telemetry_dots(mysql)
    emit('lastMarkers', {'gprs': gprs,'aprs':aprs, 'telemetry': telemetry}, namespace='/mcc')

@socketio.on('Oleg', namespace='/mcc')
def msg():
    data = parsing.pars_Oleg(mysql)
    emit('lastMarkerOleg', {'Oleg': data}, namespace='/mcc')


if __name__ == '__main__':
    mysql.init_app(app)    
    if is_dev == 1:
        socketio.run(app, host='0.0.0.0', debug=True)
    else:
        socketio.run(app, host='0.0.0.0')
