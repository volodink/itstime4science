from datetime import datetime
import struct
import pymysql
import os
import json
import time
import aprslib

def toBitArray(val):
    return list(map(lambda x: 'false' if (x == '0') else 'ok', '{0:04}'.format(val)))


def run(number):
    print(toBitArray(number))
    print(len(toBitArray(number)))
    return toBitArray(number)


def callback(packet):
    packet = packet.decode('utf-8')
    if '# aprsc' in packet:
        print('Отчёт: ' + packet)
    elif '# javAPRSSrvr' in packet:
        print('Отчёт: ' + packet)
    elif 'UB4FEU-11>UB4FEU' in packet:
        print('Данные апрс: ' + packet)
        d=[]
        if "UB4FEU-11>UB4FEU,R4FBA-1*,WIDE1*,WIDE2-2,qAR,RA4FHE-1:T#" in packet:
            d = packet.split("UB4FEU-11>UB4FEU,R4FBA-1*,WIDE1*,WIDE2-2,qAR,RA4FHE-1:T#")
            print('Апрс пришёл по формату "UB4FEU-11>UB4FEU,R4FBA-1*,WIDE1*,WIDE2-2,qAR,RA4FHE-1:T#" + данные')
        elif "UB4FEU-11>UB4FEU,WIDE1-1,WIDE2-2,qAR,RA4FHE-1:T#" in packet:
            d = packet.split("UB4FEU-11>UB4FEU,WIDE1-1,WIDE2-2,qAR,RA4FHE-1:T#")
            print('Апрс пришёл по формату "UB4FEU-11>UB4FEU,WIDE1-1,WIDE2-2,qAR,RA4FHE-1:T#" + данные')
        else: print('Чё происходит? Данные по апрс пришли какие-то странные')
        try:
            print(d)
            d = d[1].split(',')
            tm = time.localtime()
            tm = time.strftime("%Y%m%d%H%M%S", tm)
            print('Время прибытия данных: ' + tm)
            d.insert(0,tm)
            d.insert(0,10001)
            d[8] = run(int(d[8]))
            print('Распаршенные данные апрс: ' + str(d))
            try:
                db = pymysql.connect(host=os.getenv("MYSQL_DATABASE_HOST", "0"),
                                     port=int(os.getenv("MYSQL_DATABASE_PORT", "0")),
                                     user=os.getenv("MYSQL_DATABASE_USER", "0"),
                                     passwd=os.getenv("MYSQL_DATABASE_PASSWORD", "0"), db=os.getenv("MYSQL_DATABASE_DB", "0"),
                                     charset='utf8')

                cursor = db.cursor()

                insert = """INSERT INTO aprs(numberOfFlight, datetime, lat, lon, alt, temp1, pressure1, status) VALUES({},'{}',{},{},{},{},{},'{}')""".format(d[0], d[1],d[3], d[4], d[5],d[6],d[7],','.join(d[8]))
                cursor.execute(insert)
                db.commit()
                print('Попытка сохранения данных aprs в бд завершилась успешно')

            except:
                print('Попытка сохранения данных aprs в бд провалилась')
        except:
            print('распарсить не удалось, возможно не наши данные')
    else: pass
         	