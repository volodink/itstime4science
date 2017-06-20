from datetime import datetime
import struct
import pymysql
import os


def clear_string(str):
    new_str = ''
    for s in str:
        return s

def read_data(file,n):
    var = []
    var = file.read(n)
    return var


def toBitArray(val):
    return list(map(lambda x: 'false' if (x == '0') else 'ok', '{0:020b}'.format(val)))


def run(number):
    print(toBitArray(number))
    print(len(toBitArray(number)))
    return toBitArray(number)


def insert(packet):
    try:
        f = open('logs/formated_gprs.log', 'a+')
        i = 0
        data = packet[0:3]
        d = []

        data = 10001  # numberOfFlightmysql
        d.append(data)

        data = packet[3:4]  # sats
        d.append(int.from_bytes(data, byteorder='little'))

        data = packet[4:8]  # time
        data = int.from_bytes(data, byteorder='little')
        data = datetime.fromtimestamp(data)
        data = str(data)
        d.append(data)

        data = packet[8:12]  # status
        databin = int.from_bytes(data, byteorder='little')
        l = run(databin)
        d.append(l)

        data = packet[12:16]  # lat
        data = struct.unpack('f', data)
        d.append(clear_string(data))

        data = packet[16:20]  # lon
        data = struct.unpack('f', data)
        d.append(clear_string(data))

        data = packet[20:24]  # alt
        data = struct.unpack('f', data)
        d.append(clear_string(data))

        data = packet[24:28]  # temp1
        data = struct.unpack('f', data)
        d.append(clear_string(data))

        data = packet[28:32]  # temp2
        data = struct.unpack('f', data)
        d.append(clear_string(data))

        data = packet[32:36]  # pressure1
        data = struct.unpack('f', data)
        d.append(clear_string(data))

        data = packet[36:40]  # pressure2
        data = struct.unpack('f', data)
        d.append(clear_string(data))

        data = packet[40:44]  # bat_volt
        data = struct.unpack('f', data)
        d.append(clear_string(data))

        data = packet[44:48]  # bat_temp
        data = struct.unpack('f', data)
        d.append(clear_string(data))

        data = packet[48:52]  # vect_axel1x
        data = struct.unpack('f', data)
        d.append(clear_string(data))

        data = packet[52:56]  # vect_axel1y
        data = struct.unpack('f', data)
        d.append(clear_string(data))

        data = packet[56:60]  # vect_axel1z
        data = struct.unpack('f', data)
        d.append(clear_string(data))

        data = packet[60:64]  # vect_axel2x
        data = struct.unpack('f', data)
        d.append(clear_string(data))

        data = packet[64:68]  # vect_axel2y
        data = struct.unpack('f', data)
        d.append(clear_string(data))

        data = packet[68:72]  # vect_axel2z
        data = struct.unpack('f', data)
        d.append(clear_string(data))

        data = packet[72:76]  # ultraviolet1
        data = struct.unpack('f', data)
        d.append(clear_string(data))

        data = packet[76:80]  # ultraviolet2
        data = struct.unpack('f', data)
        d.append(clear_string(data))

        data = packet[80:84]  # infrared1
        data = struct.unpack('f', data)
        d.append(clear_string(data))

        data = packet[84:88]  # infrared2
        data = struct.unpack('f', data)
        d.append(clear_string(data))

        data = packet[88:92]  # hdop
        data = struct.unpack('f', data)
        d.append(clear_string(data))

        data = packet[92:96]  # vdop
        data = struct.unpack('f', data)
        d.append(clear_string(data))


        data = packet[96:100]  # radiation
        data = struct.unpack('f', data)
        d.append(clear_string(data))

        data = packet[100:104]  # dust
        data = struct.unpack('f', data)
        d.append(clear_string(data))

        data = packet[104:108]  # ozone
        data = struct.unpack('f', data)
        d.append(clear_string(data))


        print(d[27])
        print(len(d))
        for i in range(len(d)):
            f.write(str(d[i]) + '    ')
        f.write('\n')
        f.close()
        try:
            db = pymysql.connect(host=os.getenv("MYSQL_DATABASE_HOST", "0"),
                                 port=int(os.getenv("MYSQL_DATABASE_PORT", "0")),
                                 user=os.getenv("MYSQL_DATABASE_USER", "0"),
                                 passwd=os.getenv("MYSQL_DATABASE_PASSWORD", "0"), db=os.getenv("MYSQL_DATABASE_DB", "0"),
                                 charset='utf8')

            cursor = db.cursor()

            print('Принятый пакет:' + str(d))

            insert = """INSERT INTO gprs(numberOfFlight, sats,datetime,status, lat, lon,alt,temp1,temp2,pressure1,pressure2,\
                    bat_volt,bat_temp,vect_axel1x,vect_axel1y,vect_axel1z,vect_axel2x,vect_axel2y,vect_axel2z,ultraviolet1,ultraviolet2,\
                    infrared1,infrared2,hdop,vdop,radiation,dust,ozone) VALUES({},{}, {}, '{}', '{}', {}, {}, {}, {}, {}, {}, \
                    {}, {}, {}, {}, {}, {}, {}, {}, {}, {},{}, {}, {}, {}, {}, {}, {}, {})""".format(d[0], d[1],
                                                                                                       d[2], ','.join(d[3]), d[4],
                                                                                                       d[5], d[6], d[7], d[8],
                                                                                                       d[9], d[10], d[11],
                                                                                                       d[12], d[13], d[14],
                                                                                                       d[15], d[16], d[17],
                                                                                                       d[18], d[19], d[20],
                                                                                                       d[21], d[22],d[23],
                                                                                                       d[24], d[25], d[26],
                                                                                                       d[27])
            cursor.execute(insert)

            db.commit()

            #cursor.execute("select * from gprs")

            #data = cursor.fetchall()
            f.close()
            print('Попытка сохранения данных gprs в бд завершилась успешно')

        except:
            print('Попытка сохранения данных gprs в бд провалилась')

    except struct.error:
        print("Пакет не полный. Записан его исходный вариант в логи")
