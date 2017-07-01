import json
from flask import Flask, request, render_template
import html
import base64
from datetime import datetime
from flask.ext.mysql import MySQL
import pymysql
import os
def toBitArray(val):
    return list(map(lambda x: 'false' if (x == '0') else 'ok', '{0:04}'.format(val)))


def run(number):
    print(toBitArray(number))
    print(len(toBitArray(number)))
    return toBitArray(number)


def pars_gprs(mysql):
    try:
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
            e['hdop'] = element[14]
            e['vdop'] = element[15]
            e['sats'] = element[16]
            e['radiation'] = element[17]
            r.append(e)
            return json.dumps(r)
    except:
        return 0
def pars_telemetry(mysql):
    try:
        cur = mysql.connect().cursor()
        cur.execute("select * from telemetry ORDER BY id DESC LIMIT 1")
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
            e['hdop'] = element[14]
            e['vdop'] = element[15]
            e['sats'] = element[16]
            e['radiation'] = element[17]

            r.append(e)

            return json.dumps(r)
    except:
        return 0

def pars_aprs(mysql):
    try:
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

            r.append(e)

            return json.dumps(r)
    except:
        return 0


def last_gprs_dots(mysql):
    try:
        cur = mysql.connect().cursor()
        r = []
        cur.execute("select lat,lon from gprs ORDER BY id DESC LIMIT 10", )
        data = list(cur.fetchall())

        mysql.connect().commit
        for element in data:
            e = dict()
            e['lat'] = element[0]
            e['lon'] = element[1]
            r.append(e)
        return json.dumps(r)
    except:
        return 'Nan'

def last_aprs_dots(mysql):
    try:
        cur = mysql.connect().cursor()
        r = []
        cur.execute("select lat,lon from aprs ORDER BY id DESC LIMIT 10", )
        data = list(cur.fetchall())

        mysql.connect().commit
        for element in data:
            e = dict()
            e['lat'] = element[0]
            e['lon'] = element[1]
            r.append(e)
        return json.dumps(r)
    except:
        return 'Nan'

def last_telemetry_dots(mysql):
    try:
        cur = mysql.connect().cursor()
        r = []
        cur.execute("select lat,lon from telemetry ORDER BY id DESC LIMIT 10", )
        data = list(cur.fetchall())

        mysql.connect().commit
        for element in data:
            e = dict()
            e['lat'] = element[0]
            e['lon'] = element[1]
            r.append(e)
        return json.dumps(r)
    except:
        return 'Nan'

def write_in_file(f, mas):
    f.write(str(mas) + '\n')
    f.close()


def parsing_telem(mysql):
    try:

        kek = html.escape(request.args.get('bs64', ''))
        kek = kek + '==='
        kek = kek.encode('utf-8')
        print(kek)
        kek = base64.b64decode(kek)
        kek = kek.decode('utf-8')
        try:
            f = open('logs/telemetry_all_logs.log', 'a+')
            write_in_file(f, kek)
            try:
                kek = kek.split(';')
                result = kek
                kek.pop(0)
                kek.insert(0, 10001)
                print(kek)
                kek[2] = datetime.fromtimestamp(int(kek[2]))

                try:
                    db = pymysql.connect(host=os.getenv("MYSQL_DATABASE_HOST", "0"),
                                 port=int(os.getenv("MYSQL_DATABASE_PORT", "0")),
                                 user=os.getenv("MYSQL_DATABASE_USER", "0"),
                                 passwd=os.getenv("MYSQL_DATABASE_PASSWORD", "0"), db=os.getenv("MYSQL_DATABASE_DB", "0"),
                                 charset='utf8')


                    cursor = db.cursor()
                    insert ="""INSERT INTO telemetry(numberOfFlight, sats,datetime, lat, lon,alt,temp1,temp2,pressure1,pressure2,\
                                            bat_volt,vect_axel1x,vect_axel1y,vect_axel1z,hdop,vdop,radiation)\
                                             VALUES({},{}, '{}', {}, {}, {}, {}, {}, {}, {},  \
                                            {}, {}, {}, {}, {}, {}, {})""".format(int(kek[0]), int(kek[1]), kek[2],
                                                                                                         float(kek[3]), float(kek[4]),
                                                                                                         float(kek[5]), float(kek[6]),
                                                                                                         float(kek[7]), float(kek[8]),
                                                                                                         float(kek[9]), float(kek[10]),
                                                                                                         float(kek[11]),
                                                                                                         float(kek[12]), float(kek[13]),
                                                                                                         float(kek[14]),
                                                                                                         float(kek[15]), float(kek[16]))
                    cursor.execute(insert)
                    db.commit()
                            
                    try:
                        f = open('logs/telemetry_NOT_fails.log', 'a+')
                        write_in_file(f, kek)
                        return render_template('telem.html', kek=result)
                    except:
                        return render_template('telem.html',
                                               kek='Не удалось сохранить логи в файл, хотя пакет данных валиден.')

                except:
                    return render_template('telem.html',
                                           kek='Не удалось сохранить в базу данных. Проверьте порядок данных, их тип, а так же валидность данных для входа в бд.')
            except:
                return render_template('telem.html', kek='Принятый пакет не удалось распарсить.')
        except:
            return render_template('telem.html',
                                   kek='Не удалось сохранить логи в файл, пакет был конвертирован, но не распаршен.')

    except:
        f = open('logs/telemetry_fails.log', 'a+')
        write_in_file(f, kek)
        return render_template('telem.html', kek='Данные фейловые и будут записаны в лог файл')
