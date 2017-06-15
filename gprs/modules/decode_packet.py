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

        data = packet[3:4]  # bat_crg
        d.append(int.from_bytes(data, byteorder='little'))

        data = packet[4:5]  # sats
        d.append(int.from_bytes(data, byteorder='little'))

        data = packet[5:9]  # time
        data = int.from_bytes(data, byteorder='little')
        data = datetime.fromtimestamp(data)
        data = str(data)
        d.append(data)

        data = packet[9:13]  # status
        databin = int.from_bytes(data, byteorder='little')
        l = run(databin)
        d.append(l)

        data = packet[13:17]  # lat
        data = struct.unpack('f', data)
        d.append(clear_string(data))

        data = packet[17:21]  # lon
        data = struct.unpack('f', data)
        d.append(clear_string(data))

        data = packet[21:25]  # alt
        data = struct.unpack('f', data)
        d.append(clear_string(data))

        data = packet[25:29]  # temp1
        data = struct.unpack('f', data)
        d.append(clear_string(data))

        data = packet[29:33]  # temp2
        data = struct.unpack('f', data)
        d.append(clear_string(data))

        data = packet[33:37]  # pressure1
        data = struct.unpack('f', data)
        d.append(clear_string(data))

        data = packet[37:41]  # pressure2
        data = struct.unpack('f', data)
        d.append(clear_string(data))

        data = packet[41:45]  # bat_volt
        data = struct.unpack('f', data)
        d.append(clear_string(data))

        data = packet[45:49]  # bat_temp
        data = struct.unpack('f', data)
        d.append(clear_string(data))

        data = packet[49:53]  # vect_axel1x
        data = struct.unpack('f', data)
        d.append(clear_string(data))

        data = packet[53:57]  # vect_axel1y
        data = struct.unpack('f', data)
        d.append(clear_string(data))

        data = packet[57:61]  # vect_axel1z
        data = struct.unpack('f', data)
        d.append(clear_string(data))

        data = packet[61:65]  # vect_axel2x
        data = struct.unpack('f', data)
        d.append(clear_string(data))

        data = packet[65:69]  # vect_axel2y
        data = struct.unpack('f', data)
        d.append(clear_string(data))

        data = packet[69:73]  # vect_axel2z
        data = struct.unpack('f', data)
        d.append(clear_string(data))

        data = packet[73:77]  # ultraviolet1
        data = struct.unpack('f', data)
        d.append(clear_string(data))

        data = packet[77:81]  # ultraviolet2
        data = struct.unpack('f', data)
        d.append(clear_string(data))

        data = packet[81:85]  # infrared1
        data = struct.unpack('f', data)
        d.append(clear_string(data))

        data = packet[85:89]  # infrared2
        data = struct.unpack('f', data)
        d.append(clear_string(data))

        data = packet[89:93]  # hdop
        data = struct.unpack('f', data)
        d.append(clear_string(data))

        data = packet[93:97]  # vdop
        data = struct.unpack('f', data)
        d.append(clear_string(data))


        data = packet[97:101]  # radiation
        data = struct.unpack('f', data)
        d.append(clear_string(data))

        data = packet[101:105]  # dust
        data = struct.unpack('f', data)
        d.append(clear_string(data))

        data = packet[105:109]  # ozone
        data = struct.unpack('f', data)
        d.append(clear_string(data))


        print(d[28])
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

            insert = """INSERT INTO gprs(numberOfFlight, bat_crg,sats,datetime,status, lat, lon,alt,temp1,temp2,pressure1,pressure2,\
                    bat_volt,bat_temp,vect_axel1x,vect_axel1y,vect_axel1z,vect_axel2x,vect_axel2y,vect_axel2z,ultraviolet1,ultraviolet2,\
                    infrared1,infrared2,hdop,vdop,radiation,dust,ozone) VALUES({},{}, {}, '{}', '{}', {}, {}, {}, {}, {}, {}, \
                    {}, {}, {}, {}, {}, {}, {}, {}, {}, {},{}, {}, {}, {}, {}, {}, {}, {})""".format(d[0], d[1], d[2],
                                                                                                       d[3], ','.join(d[4]), d[5],
                                                                                                       d[6], d[7], d[8], d[9],
                                                                                                       d[10], d[11], d[12],
                                                                                                       d[13], d[14], d[15],
                                                                                                       d[16], d[17], d[18],
                                                                                                       d[19], d[20], d[21],
                                                                                                       d[22], d[23],d[24],
                                                                                                       d[25], d[26], d[27],
                                                                                                       d[28])
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
