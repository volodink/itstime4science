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
