import json
from flask import Flask
from flask.ext.mysql import MySQL

def gprs(mysql):
    cur = mysql.connect().cursor()
    cur.execute("select * from gprs WHERE numberOfFlight = 10001")
    data = list(cur.fetchall())
    mysql.connect().commit
    #print(data)
    i=0
    r=[]
    w =[]
    for element in data:
        e = dict()
        ['id'] = element[0]
        e['numberOfFlight'] = element[1]
        e['datetime'] = str(element[2])
        e['lat'] = element[3]
        e['lon'] = element[4]
        e['alt'] = element[5]
        e['temp1'] = element[6]
        e['pressure1'] = element[7]
        e['pressure2'] = element[8]
        e['bat_volt'] = element[9]
        e['vect_axel1x'] = element[10]
        e['vect_axel1y'] = element[11]
        e['vect_axel1z'] = element[12]
        e['hdop'] = element[13]
        e['vdop'] = element[14]
        e['sats'] = element[15]
        
        r.append(e)
    w.append(json.dumps(r))
    #print(json.dumps(w))
    return json.dumps(w)

def telemetry(mysql):
    cur = mysql.connect().cursor()
    cur.execute("select * from telemetry WHERE numberOfFlight = 10001")
    data = list(cur.fetchall())
    mysql.connect().commit
    #print(data)
    i=0
    r=[]
    w =[]
    for element in data:
        e = dict()
        ['id'] = element[0]
        e['numberOfFlight'] = element[1]
        e['datetime'] = str(element[2])
        e['lat'] = element[3]
        e['lon'] = element[4]
        e['alt'] = element[5]
        e['temp1'] = element[6]
        e['pressure1'] = element[7]
        e['pressure2'] = element[8]
        e['bat_volt'] = element[9]
        e['vect_axel1x'] = element[10]
        e['vect_axel1y'] = element[11]
        e['vect_axel1z'] = element[12]
        e['hdop'] = element[13]
        e['vdop'] = element[14]
        e['sats'] = element[15]
        r.append(e)
    w.append(json.dumps(r))
    #print(json.dumps(w))
    return json.dumps(w)

def aprs(mysql):
    cur = mysql.connect().cursor()
    cur.execute("select * from aprs WHERE numberOfFlight = 10001")
    data = list(cur.fetchall())
    mysql.connect().commit
    #print(data)
    i=0
    r=[]
    w =[]
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
    w.append(json.dumps(r))
    #print(json.dumps(w))
    return json.dumps(w)
