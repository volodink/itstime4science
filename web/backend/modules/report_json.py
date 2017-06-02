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
        e['bat_crg'] = element[10]
        e['bat_volt'] = element[11]
        e['bat_temp'] = element[12]
        e['vect_axel1x'] = element[13]
        e['vect_axel1y'] = element[14]
        e['vect_axel1z'] = element[15]
        e['vect_axel2x'] = element[16]
        e['vect_axel2y'] = element[17]
        e['vect_axel2z'] = element[18]
        e['ultraviolet1'] = element[19]
        e['ultraviolet2'] = element[20]
        e['infrared1'] = element[21]
        e['infrared2'] = element[22]
        e['hdop'] = element[23]
        e['vdop'] = element[24]
        e['sats'] = element[25]
        e['radiation'] = element[26]
        e['dust'] = element[27]
        e['ozone'] = element[28]
        e['status'] = dict()

        s = element[29].split(',')
        e['status']['datetime'] = s[0]
        e['status']['lat'] = s[1]
        e['status']['lon'] = s[1]
        e['status']['alt'] = s[1]
        e['status']['temp1'] = s[2]
        e['status']['temp2'] = s[3]
        e['status']['pressure1'] = s[4]
        e['status']['pressure2'] = s[5]
        e['status']['bat_crg'] = s[6]
        e['status']['bat_volt'] = s[7]
        e['status']['bat_temp'] = s[8]
        e['status']['vect_axel1x'] = s[9]
        e['status']['vect_axel1y'] = s[9]
        e['status']['vect_axel1z'] = s[9]
        e['status']['vect_axel2x'] = s[10]
        e['status']['vect_axel2y'] = s[10]
        e['status']['vect_axel2z'] = s[10]
        e['status']['ultraviolet1'] = s[11]
        e['status']['ultraviolet2'] = s[12]
        e['status']['infrared1'] = s[13]
        e['status']['infrared2'] = s[14]
        e['status']['hdop'] = s[15]
        e['status']['vdop'] = s[16]
        e['status']['sats'] = s[17]
        e['status']['radiation'] = s[18]
        e['status']['ozone'] = s[19]
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
        e['bat_crg'] = element[10]
        e['bat_volt'] = element[11]
        e['bat_temp'] = element[12]
        e['vect_axel1x'] = element[13]
        e['vect_axel1y'] = element[14]
        e['vect_axel1z'] = element[15]
        e['vect_axel2x'] = element[16]
        e['vect_axel2y'] = element[17]
        e['vect_axel2z'] = element[18]
        e['ultraviolet1'] = element[19]
        e['ultraviolet2'] = element[20]
        e['infrared1'] = element[21]
        e['infrared2'] = element[22]
        e['hdop'] = element[23]
        e['vdop'] = element[24]
        e['sats'] = element[25]
        e['radiation'] = element[26]
        e['dust'] = element[27]
        e['ozone'] = element[28]
        e['status'] = dict()

        #s = element[29].split(',')
        #e['status']['datetime'] = s[0]
        #e['status']['lat'] = s[1]
        #e['status']['lon'] = s[1]
        #e['status']['alt'] = s[1]
        #e['status']['temp1'] = s[2]
        #e['status']['temp2'] = s[3]
        #e['status']['pressure1'] = s[4]
        #e['status']['pressure2'] = s[5]
        #e['status']['bat_crg'] = s[6]
        #e['status']['bat_volt'] = s[7]
        #e['status']['bat_temp'] = s[8]
        #e['status']['vect_axel1x'] = s[9]
        #e['status']['vect_axel1y'] = s[9]
        #e['status']['vect_axel1z'] = s[9]
        #e['status']['vect_axel2x'] = s[10]
        #e['status']['vect_axel2y'] = s[10]
        #e['status']['vect_axel2z'] = s[10]
        #e['status']['ultraviolet1'] = s[11]
        #e['status']['ultraviolet2'] = s[12]
        #e['status']['infrared1'] = s[13]
        #e['status']['infrared2'] = s[14]
        #e['status']['hdop'] = s[15]
        #e['status']['vdop'] = s[16]
        #e['status']['sats'] = s[17]
        #e['status']['radiation'] = s[18]
        #e['status']['ozone'] = s[19]
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
        e['temp'] = element[6]
        e['pressure'] = element[7]
        e['status'] = dict()

        s = element[8].split(',')
        e['status']['datetime'] = s[0]
        e['status']['lat'] = s[1]
        e['status']['lon'] = s[1]
        e['status']['alt'] = s[1]
        e['status']['temp'] = s[2]
        e['status']['pressure'] = s[3]
        e['status']['modul'] = s[4]
        r.append(e)
    w.append(json.dumps(r))
    #print(json.dumps(w))
    return json.dumps(w)
