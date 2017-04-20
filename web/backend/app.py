from flask import Flask, render_template
from flask_mysqldb import MySQL

import sys
import os
import content
from flask_socketio import SocketIO
from flask_socketio import send, emit



# get env variable to differ dev version from prod
is_dev = int(os.getenv("DEV", "0"))

sys.path.append(str(os.path.abspath(sys.argv[0])))

from params import Parser

mysql = MySQL(app)
app = Flask(__name__)
app.template_folder = '../frontend/templates/'
app.static_folder = "../frontend/static/"
app.config['SECRET_KEY'] = 'secret'
app.config['MYSQL_DATABASE_USER'] = ''
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = ''
app.config['MYSQL_DATABASE_HOST'] = ''
socketio = SocketIO(app)
mysql.init_app(app)
cursor = mysql.connection.cursor()

data = content.getContent()
# Новый контент можно добавить в файл
# /web/backend/content.py

namespace = Parser().createParser().parse_args(sys.argv[1:])
def parsing_of_data(cursor):
    data = cursor.execute('''SELECT numberOfFlight,datetime,lat,lon,alt,temp1,temp2,pressure1,pressure2,bat_crg,bat_volt,bat_temp,vect_axel1,\
vect_axel2,ultraviolet1,ultraviolet2,infrared1,infrared2,hdop,vdop,sats,radiation,dust,ozone, host FROM mysql.root''')
    data = data.split(',')
    numberOfFlight = data[0]
    datatime = data[1]
    lat = data[2]
    lon = data[3]
    alt = data[4]
    temp1 = data[5]
    temp2 = data[6]
    pressure1 = data[7]
    pressure2 = data[8]
    bat_crg = data[9]
    bat_volt = data[10]
    bat_temp = data[11]
    vect_axel1 = data[12]
    vect_axel2 = data[13]
    ultraviolet1 = data[14]
    ultraviolet2 = data[15]
    infrared1 = data[16]
    infrared2 = data[17]
    hdop = data[18]
    vdop = data[19]
    sats = data[20]
    radiation = data[21]
    dust = data[22]
    ozone = data[23]
    return numberOfFlight, datatime, lat, lon, alt, temp1, temp2, pressure1, pressure2, bat_crg, bat_volt, bat_temp, vect_axel1, vect_axel2, \
           ultraviolet1, ultraviolet2, infrared1, infrared2, hdop, vdop, sats, radiation, dust, ozone
def parsing_of_status(cursor):
    status = cursor.execute('''SELECT status, host FROM mysql.root''')
    status = status.split(',')
    datatime = status[0]
    lat = status[1]
    lon= status[2]
    alt = status[3]
    temp1 = status[4]
    temp2 = status[5]
    pressure1 = status[6]
    pressure2 = status[7]
    bat_crg = status[8]
    bat_volt = status[9]
    bat_temp = status[10]
    vect_axel1= status[11]
    vect_axel2= status[12]
    ultraviolet1= status[13]
    ultraviolet2= status[14]
    infrared1= status[15]
    infrared2= status[16]
    hdop= status[17]
    vdop= status[18]
    sats= status[19]
    radiation= status[20]
    dust= status[21]
    ozone= status[22]
    return datatime, lat, lon, alt,temp1,temp2,pressure1,pressure2,bat_crg,bat_volt,bat_temp,vect_axel1,vect_axel2,\
           ultraviolet1,ultraviolet2,infrared1,infrared2,hdop,vdop,sats,radiation,dust,ozone


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

@socketio.on('connected')
def connected(cursor):
    print("%s connected" % (request.namespace.socket.sessid))
    clients.append(request.namespace)

    datatime, lat, lon, alt, temp1, temp2, pressure1, pressure2, bat_crg, bat_volt, bat_temp, vect_axel1, vect_axel2, \
    ultraviolet1, ultraviolet2, infrared1, infrared2, hdop, vdop, sats, radiation, dust, ozone = parsing_of_status(cursor)

    socketio.emit('status', {'datatime': datatime, 'lat': lat, 'lon': lon , 'alt': alt, 'temp1': temp1, 'temp2':temp2, 'pressure1': pressure1,\
                             'pressure2': pressure2, 'bat_crg': bat_crg, 'bat_volt': bat_volt, 'bat_temp': bat_temp, 'vect_axel1': vect_axel1,\
                             'vect_axel2': vect_axel2, 'ultraviolet1': ultraviolet1, 'ultraviolet2': ultraviolet2, 'infrared1': infrared1,\
                             'infrared2': infrared2, 'hdop': hdop, 'vdop': vdop, 'sats': sats, 'radiation': radiation, 'dust': dust, 'ozone': ozone})

    numberOfFlight, datatime, lat, lon, alt, temp1, temp2, pressure1, pressure2, bat_crg, bat_volt, bat_temp, vect_axel1, vect_axel2, \
    ultraviolet1, ultraviolet2, infrared1, infrared2, hdop, vdop, sats, radiation, dust, ozone = parsing_of_data(
        cursor)

    socketio.emit('data',
                  {'numberOfFlight': numberOfFlight, 'datatime': datatime, 'lat': lat, 'lon': lon, 'alt': alt, 'temp1': temp1, 'temp2': temp2,
                   'pressure1': pressure1, 'pressure2': pressure2, 'bat_crg': bat_crg, 'bat_volt': bat_volt, 'bat_temp': bat_temp,
                   'vect_axel1': vect_axel1, 'vect_axel2': vect_axel2, 'ultraviolet1': ultraviolet1, 'ultraviolet2': ultraviolet2,\
                   'infrared1': infrared1, 'infrared2': infrared2, 'hdop': hdop, 'vdop': vdop, 'sats': sats, 'radiation': radiation,\
                   'dust': dust, 'ozone': ozone})

@socketio.on('disconnect')
def disconnect():
    print("%s disconnected" % (request.namespace.socket.sessid))


def status_from_packet (cursor):
    clients.remove(request.namespace)

if __name__ == "__main__":
    if is_dev == 1:
        socketio.run(app)
    else:
	    socketio.run(app)
	    app.run(host='{}'.format(namespace.ip), port=namespace.port)


