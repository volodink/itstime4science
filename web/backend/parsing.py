import json
from flask import Flask
from flask.ext.mysql import MySQL
def getData(mysql):
    cur = mysql.connect().cursor()
    cur.execute('''select * from gprs''')
    data = list(cur.fetchall())

    r = []
    for element in data:
        e = dict()
        e['id'] = element[0]
        e['flight_id'] = element[1]
        e['timestamp'] = str(element[2])
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
        e['status']['rtc'] = s[0]
        e['status']['gps'] = s[1]
        e['status']['termometr1'] = s[2]
        e['status']['termometr2'] = s[3]
        e['status']['barometr1'] = s[4]
        e['status']['barometr2'] = s[5]
        e['status']['bat_crg'] = s[6]
        e['status']['bat_volt'] = s[7]
        e['status']['bat_temp'] = s[8]
        e['status']['vect_axel1'] = s[9]
        e['status']['vect_axel2'] = s[10]
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

        return json.dumps(r)
