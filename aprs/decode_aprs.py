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
def write_in_file(f,mas):
    f.write(str(mas) + '\n')
    f.close()
def lets_try_pars(d):
    try:

        print(d)
        d = d[1].split(',')
        tm = time.localtime()
        tm = time.strftime("%Y%m%d%H%M%S", tm)
        print('Время прибытия данных: ' + tm)
        d.insert(0,tm)
        d.insert(0,10001)

        print('Распаршенные данные апрс: ' + str(d))
        try:
            db = pymysql.connect(host=os.getenv("MYSQL_DATABASE_HOST", "0"),
                                 port=int(os.getenv("MYSQL_DATABASE_PORT", "0")),
                                 user=os.getenv("MYSQL_DATABASE_USER", "0"),
                                 passwd=os.getenv("MYSQL_DATABASE_PASSWORD", "0"), db=os.getenv("MYSQL_DATABASE_DB", "0"),
                                 charset='utf8')

            cursor = db.cursor()

            insert = """INSERT INTO aprs(numberOfFlight, datetime, lat, lon, alt, temp1, pressure1) VALUES({},'{}',{},{},{},{},{})""".format(d[0], d[1], d[2],d[3], d[4], d[5],d[6])
            cursor.execute(insert)
            db.commit()
            print('Попытка сохранения данных aprs в бд завершилась успешно')
            try:
                f = open('logs/aprs_FORMATED(normal).log', 'a+')
                write_in_file(f, d)
            except: print('Попытка сохранить логи провалилась')
        except:
            print('Попытка сохранения данных aprs в бд провалилась')
    except:
        print('Распарсить не удалось, возможно не наши данные')

def callback(packet):
    packet = packet.decode('utf-8')
    if '# aprsc' in packet:
        print('Отчёт: ' + packet)
        f = open('logs/aprs_all.log', 'a+')
        write_in_file(f, packet)
    elif '# javAPRSSrvr' in packet:
        print('Отчёт: ' + packet)
        f = open('logs/aprs_all.log', 'a+')
        write_in_file(f, packet)
    elif 'UB4FEU-11>UB4FEU' in packet:
        print('Данные апрс: ' + packet)
        d=[]
        if "UB4FEU-11>UB4FEU,R4FBA-1*,WIDE1*,WIDE2-2,qAR,RA4FHE-1:T#" in packet:
            d = packet.split("UB4FEU-11>UB4FEU,R4FBA-1*,WIDE1*,WIDE2-2,qAR,RA4FHE-1:T#")
            print('Апрс пришёл по формату "UB4FEU-11>UB4FEU,R4FBA-1*,WIDE1*,WIDE2-2,qAR,RA4FHE-1:T#" + данные')
            lets_try_pars(d)
        elif "UB4FEU-11>UB4FEU,WIDE1-1,WIDE2-2,qAR,RA4FHE-1:T#" in packet:
            d = packet.split("UB4FEU-11>UB4FEU,WIDE1-1,WIDE2-2,qAR,RA4FHE-1:T#")
            print('Апрс пришёл по формату "UB4FEU-11>UB4FEU,WIDE1-1,WIDE2-2,qAR,RA4FHE-1:T#" + данные')
            lets_try_pars(d)
        else: 
            f = open('logs/aprs_FAIL.log', 'a+')
            write_in_file(f, packet)
            print('Чё происходит? Данные по апрс пришли какие-то странные, я не буду их записывать! (Только в лог файл)')
    elif ' UB4FEU-6>' in packet:
        try:
                s = aprslib.parse(packet)
                try:
                    db = pymysql.connect(host=os.getenv("MYSQL_DATABASE_HOST", "0"),
                                         port=int(os.getenv("MYSQL_DATABASE_PORT", "0")),
                                         user=os.getenv("MYSQL_DATABASE_USER", "0"),
                                         passwd=os.getenv("MYSQL_DATABASE_PASSWORD", "0"), db=os.getenv("MYSQL_DATABASE_DB", "0"),
                                         charset='utf8')

                    cursor = db.cursor()

                    insert = """INSERT INTO Oleg(lat, lon) VALUES({},{})""".format(s['latitude'], s['longitude'])
                    cursor.execute(insert)
                    db.commit()
                except:
                    print('Не удалось сохранить в бд')
        except:
            print('Парсинг координат пользователя не удался')

    else: pass
         	