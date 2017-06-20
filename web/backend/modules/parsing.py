import json
from flask import Flask,request,render_template
import html
from datetime import datetime
from flask.ext.mysql import MySQL
def pars_gprs(mysql):
    cur = mysql.connect().cursor()
    cur.execute("select * from gprs ORDER BY id DESC LIMIT 1")
    data = list(cur.fetchall())
    mysql.connect().commit
    r = []
    for element in data:
        e = dict()
        e['id'] = element[0]
        e['numberOfFlight'] = element[1]
        e['datetime'] = str(element[2])
        e['lat'] = element[3]
        e['lon'] = element[4]
        e['alt'] = element[5]
        e['temp1'] = element[6]
        e['temp2'] = element[7]
        e['pressure1'] = element[8]
        e['pressure2'] = element[9]
        e['bat_volt'] = element[10]
        e['bat_temp'] = element[11]
        e['vect_axel1x'] = element[12]
        e['vect_axel1y'] = element[13]
        e['vect_axel1z'] = element[14]
        e['vect_axel2x'] = element[15]
        e['vect_axel2y'] = element[16]
        e['vect_axel2z'] = element[17]
        e['ultraviolet1'] = element[18]
        e['ultraviolet2'] = element[19]
        e['infrared1'] = element[20]
        e['infrared2'] = element[21]
        e['hdop'] = element[22]
        e['vdop'] = element[23]
        e['sats'] = element[24]
        e['radiation'] = element[25]
        e['dust'] = element[26]
        e['ozone'] = element[27]
        e['status'] = dict()

        s = element[28].split(',')
        e['status']['datetime'] = s[0]
        e['status']['lat'] = s[1]
        e['status']['lon'] = s[1]
        e['status']['alt'] = s[1]
        e['status']['temp1'] = s[2]
        e['status']['temp2'] = s[3]
        e['status']['pressure1'] = s[4]
        e['status']['pressure2'] = s[5]
        e['status']['bat_volt'] = s[6]
        e['status']['bat_temp'] = s[7]
        e['status']['vect_axel1x'] = s[8]
        e['status']['vect_axel1y'] = s[8]
        e['status']['vect_axel1z'] = s[8]
        e['status']['vect_axel2x'] = s[9]
        e['status']['vect_axel2y'] = s[9]
        e['status']['vect_axel2z'] = s[9]
        e['status']['ultraviolet1'] = s[10]
        e['status']['ultraviolet2'] = s[11]
        e['status']['infrared1'] = s[12]
        e['status']['infrared2'] = s[13]
        e['status']['hdop'] = s[14]
        e['status']['vdop'] = s[15]
        e['status']['sats'] = s[16]
        e['status']['radiation'] = s[17]
        e['status']['ozone'] = s[18]
        r.append(e)

        return json.dumps(r)
def pars_aprs(mysql):
    cur = mysql.connect().cursor()
    cur.execute("select * from aprs ORDER BY id DESC LIMIT 1")
    data = list(cur.fetchall())
    mysql.connect().commit
    r = []
    for element in data:
        e = dict()
        e['id'] = element[0]
        e['numberOfFlight'] = element[1]
        e['datetime'] = str(element[2])
        e['lat'] = element[3]
        e['lon'] = element[4]
        e['alt'] = element[5]
        e['temp1'] = element[6]
        e['pressure1'] = element[7]
        e['status'] = dict()

        s = element[8].split(',') #ВОТ ТУТ УТОЧНИТЬ ПОРЯДОК СТАТУСА
        e['status']['lat'] = s[0]
        e['status']['lon'] = s[0]
        e['status']['alt'] = s[0]
        e['status']['temp1'] = s[1]
        e['status']['pressure1'] = s[2]
        e['status']['modul'] = s[3]
        r.append(e)

        return json.dumps(r)
def last_gprs_dots(mysql):
    cur = mysql.connect().cursor()
    r = []
    cur.execute("select lat,lon from gprs ORDER BY id DESC LIMIT 10",)
    data = list(cur.fetchall())

    mysql.connect().commit
    for element in data:
        e = dict()
        e['lat'] = element[0]
        e['lon'] = element[1]
        r.append(e)
    return json.dumps(r)

def last_aprs_dots(mysql):
    cur = mysql.connect().cursor()
    r = []
    cur.execute("select lat,lon from aprs ORDER BY id DESC LIMIT 10",)
    data = list(cur.fetchall())

    mysql.connect().commit
    for element in data:
        e = dict()
        e['lat'] = element[0]
        e['lon'] = element[1]
        r.append(e)
    return json.dumps(r)
def last_telemetry_dots(mysql):
    cur = mysql.connect().cursor()
    r = []
    cur.execute("select lat,lon from telemetry ORDER BY id DESC LIMIT 10",)
    data = list(cur.fetchall())

    mysql.connect().commit
    for element in data:
        e = dict()
        e['lat'] = element[0]
        e['lon'] = element[1]
        r.append(e)
    return json.dumps(r)
def parsing_telem(mysql):
    data = dict()
    data['numberOfFlight']=10001
    elements_float = ['lat', 'lon', 'alt', 'temp1', 'temp2', 'pressure1', 'pressure2', 'bat_volt', 'bat_temp','vect_axel1x' \
        , 'vect_axel1y', 'vect_axel1z', 'vect_axel2x', 'vect_axel2y', 'vect_axel2z', 'ultraviolet1', 'ultraviolet2', \
                      'infrared1', 'infrared2', 'hdop', 'vdop', 'radiation', 'dust']
    elements_int = ['datetime', 'sats','ozone', 'status']
    for el in range(len(elements_float)):
        try:
            data[elements_float[el]] = float(html.escape(request.args.get('{}'.format(elements_float[el]), '')))
        except:
            data[elements_float[el]] = 0.0
    for el in range(len(elements_int)):
        try:
            data[elements_int[el]] = int(html.escape(request.args.get('{}'.format(elements_int[el]), '')))
        except:
            data[elements_int[el]] = 0
    data['datetime'] = datetime.fromtimestamp(data['datetime'])
    conn = mysql.connect()
    cursor = conn.cursor()
    insert = "INSERT INTO telemetry(numberOfFlight, datetime, lat, lon,alt,temp1,temp2,pressure1,pressure2,\
                    bat_volt,bat_temp,vect_axel1x,vect_axel1y,vect_axel1z,vect_axel2x,vect_axel2y,vect_axel2z,ultraviolet1,ultraviolet2,\
                    infrared1,infrared2,hdop,vdop,sats,radiation,dust,ozone,status) VALUES({},'{}', {}, {}, {},  {}, {}, {}, {}, {}, \
                    {}, {}, {}, {}, {}, {}, {}, {}, {}, {},{}, {}, {}, {}, {}, {}, {}, '{}')".format(data['numberOfFlight'],data['datetime'], data['lat'], \
                    data['lon'], data['alt'],data['temp1'], data['temp2'], data['pressure1'], data['pressure2'], \
                    data['bat_volt'], data['bat_temp'], data['vect_axel1x'], data['vect_axel1y'], data['vect_axel1z'], data['vect_axel2x'], \
                    data['vect_axel2y'], data['vect_axel2z'], data['ultraviolet1'], data['ultraviolet2'], data['infrared1'], \
                    data['infrared2'], data['hdop'], data['vdop'], data['radiation'], data['sats'], data['dust'], data['ozone'],\
                    data['status'])
    cursor.execute(insert)
    conn.commit()
    cur = mysql.connect().cursor()
    cur.execute("select id from telemetry ORDER BY id DESC LIMIT 1")
    id = cur.fetchone()
    return render_template('telem.html', **data, id=id[0], type='telem')






