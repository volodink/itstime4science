from datetime import datetime
import struct
import pymysql
import os
import json


def clear_string(str):
    new_str = ''
    for s in str:
        return s

def read_data(file,n):
    var = []
    var = file.read(n)
    return var


def toBitArray(val):
    return list(map(lambda x: 'false' if (x == '0') else 'ok', '{0:04}'.format(val)))


def run(number):
    print(toBitArray(number))
    print(len(toBitArray(number)))
    return toBitArray(number)


def insert(packet):
    packet = packet.decode('utf-8')
    json_packet = json.loads(packet)

    data = json_packet['entries']
    data = data[0]
    print(type(data))
    print(type(int(data['time'])))
    try:
        i = 0
        d = []
        numberOfFlight = 10001  # numberOfFlightmysql
        d.append(numberOfFlight)
        databin = float(data['lat'])
        d.append(databin)
        databin = float(data['lng'])
        d.append(databin)
        databin = float(data['alt'])
        d.append(databin)
        databin = float(data['temp'])
        d.append(databin)
        databin = float(data['pressure'])
        d.append(databin)
        

        db = pymysql.connect(host=os.getenv("MYSQL_DATABASE_HOST", "0"),
                             port=int(os.getenv("MYSQL_DATABASE_PORT", "0")),
                             user=os.getenv("MYSQL_DATABASE_USER", "0"),
                             passwd=os.getenv("MYSQL_DATABASE_PASSWORD", "0"), db=os.getenv("MYSQL_DATABASE_DB", "0"),
                             charset='utf8')
        
        cursor = db.cursor()
        
        print('Принятый пакет:' + str(d))
        
        insert = """INSERT INTO aprs(numberOfFlight, datetime, lat, lon, alt, temp1, pressure1) VALUES({},'{}',{},{},{},{},{},'{}')""".format(d[0], d[1], d[2],d[3], d[4], d[5],d[6])
        cursor.execute(insert)
        db.commit()

    except struct.error:
        print("С апрсом чё-то не то")
