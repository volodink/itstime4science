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
        #e['status']['lat'] = s[1]
        #e['status']['lon'] = s[1]
        #e['status']['alt'] = s[1]
        #e['status']['temp1'] = s[2]
        #e['status']['temp2'] = s[3]
        #e['status']['pressure1'] = s[4]
        #e['status']['pressure2'] = s[5]
        #e['status']['bat_volt'] = s[6]
        #e['status']['vect_axel1x'] = s[7]
        #e['status']['vect_axel1y'] = s[7]
        #e['status']['vect_axel1z'] = s[7]
        #e['status']['ultraviolet1'] = s[8]
        #e['status']['ultraviolet2'] = s[9]
        #e['status']['infrared1'] = s[10]
        #e['status']['infrared2'] = s[11]
        #e['status']['hdop'] = s[12]
        #e['status']['vdop'] = s[13]
        #e['status']['sats'] = s[14]
        #e['status']['radiation'] = s[15]
        #e['status']['ozone'] = s[16]
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
        e['status'] = dict()

        s = element[8].split(',')
        e['status']['lat'] = s[0]
        e['status']['lon'] = s[0]
        e['status']['alt'] = s[0]
        e['status']['temp'] = s[1]
        e['status']['pressure'] = s[2]
        e['status']['modul'] = s[3]
        r.append(e)
    w.append(json.dumps(r))
    #print(json.dumps(w))
    return json.dumps(w)
