import json
from flask import Flask,request,render_template
import html
import base64
from datetime import datetime
from flask.ext.mysql import MySQL
def toBitArray(val):
    return list(map(lambda x: 'false' if (x == '0') else 'ok', '{0:016b}'.format(val)))

def run(number):
    print(toBitArray(number))
    print(len(toBitArray(number)))
    return toBitArray(number)

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
        e['vect_axel1x'] = element[11]
        e['vect_axel1y'] = element[12]
        e['vect_axel1z'] = element[13]
        e['ultraviolet1'] = element[14]
        e['ultraviolet2'] = element[15]
        e['infrared1'] = element[16]
        e['infrared2'] = element[17]
        e['hdop'] = element[18]
        e['vdop'] = element[19]
        e['sats'] = element[20]
        e['radiation'] = element[21]
        e['dust'] = element[22]
        e['ozone'] = element[23]
        e['status'] = dict()

        s = element[24].split(',')
        e['status']['datetime'] = s[0]
        e['status']['lat'] = s[1]
        e['status']['lon'] = s[1]
        e['status']['alt'] = s[1]
        e['status']['temp1'] = s[2]
        e['status']['temp2'] = s[3]
        e['status']['pressure1'] = s[4]
        e['status']['pressure2'] = s[5]
        e['status']['bat_volt'] = s[6]
        e['status']['vect_axel1x'] = s[7]
        e['status']['vect_axel1y'] = s[7]
        e['status']['vect_axel1z'] = s[7]
        e['status']['ultraviolet1'] = s[8]
        e['status']['ultraviolet2'] = s[9]
        e['status']['infrared1'] = s[10]
        e['status']['infrared2'] = s[11]
        e['status']['hdop'] = s[12]
        e['status']['vdop'] = s[13]
        e['status']['sats'] = s[14]
        e['status']['radiation'] = s[15]
        e['status']['ozone'] = s[16]
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
    try:
        kek = html.escape(request.args.get('bs64', ''))
        kek = kek + '==='
        kek = kek.encode('utf-8')
        print(kek)
        kek = base64.b64decode(kek)
        kek = kek.decode('utf-8')
        kek = kek.split(';')
        result = kek
        kek.pop(0)
        kek.insert(0, 10001)
        print(kek)
        kek[2] = datetime.fromtimestamp(int(kek[2]))
        kek[3] = run(int(kek[3]))
        cur = mysql.connect().cursor()
        cur.insert = "INSERT INTO telemetry(numberOfFlight, sats,datetime,status, lat, lon,alt,temp1,temp2,pressure1,pressure2,\
            bat_volt,bat_temp,vect_axel1x,vect_axel1y,vect_axel1z,ultraviolet1,ultraviolet2,\
            infrared1,infrared2,hdop,vdop,radiation,dust,ozone) VALUES({},{}, '{}', '{}', {}, {}, {}, {}, {}, {}, {}, \
            {}, {}, {}, {}, {}, {}, {}, {}, {}, {},{}, {}, {}, {}, {}, {}, {})""".format(kek[0], kek[1],kek[2],','.join(kek[3]) , kek[4],kek[5], kek[6], kek[7], kek[8],
                                                                                               kek[9], kek[10], kek[11],
                                                                                               kek[12], kek[13], kek[14],
                                                                                               kek[15], kek[16], kek[17],
                                                                                               kek[18], kek[19], kek[20],
                                                                                               kek[21], kek[22],kek[23])
        mysql.connect().commit
        cur = mysql.connect().cursor()
        cur.execute("select id from telemetry ORDER BY id DESC LIMIT 1")
        id = cur.fetchone()
        return render_template('telem.html', kek = result)

    except:
        f = open('backend/modules/telemetry_fails.log', 'a+')
        try:
            kek  = html.escape(request.args.get('bs64'))
            kek = kek + '==='
            kek = kek.encode('utf-8')
            print(kek)
            kek = base64.b64decode(kek)
            kek = kek.decode('utf-8')

            for i in range(len(kek)):
                        f.write(str(kek) + '  \n')
            f.close()
            return render_template('telem.html', kek = 'Данные фейловые и будут записаны в лог файл')
        except:
            kek  = html.escape(request.args.get('bs64'))
            
            return render_template('telem.html', kek = 'Даже распарсить не могу')
