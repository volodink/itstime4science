from datetime import datetime
import struct
import MySQL
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
        i=0
        data=packet[0:3]
        d = []

        data = 10001 #numberOfFlightmysql
        d.append(data)

        data=packet[3:7] #time
        data =int.from_bytes(data, byteorder='little')
        data = datetime.fromtimestamp(data)
        data = str(data)
        d.append(data)


        data=packet[7:11] #lat
        data = struct.unpack('f',data)
        d.append (clear_string(data))

        data = packet[11:15] #lon
        data = struct.unpack('f',data)
        d.append (clear_string(data))

        data = packet[15:19] #alt
        data = struct.unpack('f',data)
        d.append (clear_string(data))

        data = packet[19:23]#temp1
        data = struct.unpack('f',data)
        d.append (clear_string(data))

        data = packet[23:27]#temp2
        data = struct.unpack('f',data)
        d.append (clear_string(data))

        data = packet[27:31]#pressure1
        data= struct.unpack('f',data)
        d.append (clear_string(data))

        data = packet[31:35]#pressure2
        data= struct.unpack('f',data)
        d.append (clear_string(data))

        data = packet[35:36]#bat_crg
        d.append (int.from_bytes(data, byteorder='little'))

        data = packet[36:40]#bat_volt
        data= struct.unpack('f',data)
        d.append (clear_string(data))

        data = packet[40:44]#bat_temp
        data= struct.unpack('f',data)
        d.append (clear_string(data))

        data = packet[44:48]#vect_axel1x
        data= struct.unpack('f',data)
        d.append (clear_string(data))

        data = packet[48:52]#vect_axel1y
        data= struct.unpack('f',data)
        d.append (clear_string(data))

        data = packet[52:56]#vect_axel1z
        data= struct.unpack('f',data)
        d.append (clear_string(data))

        data = packet[56:60]#vect_axel2x
        data= struct.unpack('f',data)
        d.append (clear_string(data))

        data = packet[60:64]#vect_axel2y
        data= struct.unpack('f',data)
        d.append (clear_string(data))

        data = packet[64:68]#vect_axel2z
        data= struct.unpack('f',data)
        d.append (clear_string(data))

        data = packet[68:72]  # ultraviolet1
        data = struct.unpack('f', data)
        d.append(clear_string(data))

        data = packet[72:76]  # ultraviolet2
        data = struct.unpack('f', data)
        d.append(clear_string(data))

        data = packet[76:80]#infrared1
        data= struct.unpack('f',data)
        d.append (clear_string(data))

        data = packet[80:84]#infrared2
        data = struct.unpack('f',data)
        d.append (clear_string(data))

        data = packet[84:88]#hdop
        data = struct.unpack('f',data)
        d.append (clear_string(data))

        data = packet[88:92]#vdop
        data= struct.unpack('f',data)
        d.append (clear_string(data))

        data = packet[92:93]#sats
        d.append(int.from_bytes(data, byteorder='little'))

        data = packet[93:97]#radiation
        data= struct.unpack('f',data)
        d.append (clear_string(data))

        data = packet[97:101]#dust
        data= struct.unpack('f',data)
        d.append (clear_string(data))

        data = packet[101:105]#ozone
        d.append(bool(data))

        data = packet[105:109]#status
        databin = int.from_bytes(data, byteorder='little')
        l = run(databin)
        d.append(l)
        print(d[28])
        print(len(d))
        for i in range(len(d)):
            f.write(str(d[i]) + '    ')
        f.close()

        db = MySQLdb.connect(host=os.getenv("MYSQL_DATABASE_HOST", "0"), port=int(os.getenv("MYSQL_DATABASE_PORT", "0")), user=os.getenv("MYSQL_DATABASE_USER", "0"), passwd=os.getenv("MYSQL_DATABASE_PASSWORD", "0"), db=os.getenv("MYSQL_DATABASE_DB", "0"), charset='utf8')
        cursor = db.cursor()

        insert ="""INSERT INTO gprs(numbersOfFlight, datatime, lat, lon,alt,temp1,temp2,pressure1,pressure2,bat_crg,\
        bat_volt,bat_temp,vect_axel1x,vect_axel1y,vect_axel1z,vect_axel2x,vect_axel2y,vect_axel2z,ultraviolet1,ultraviolet2,\
        infrared1,infrared2,hdop,vdop,sats,radiation,dust,ozone,status) VALUES({},'{}', {}, {}, {}, {}, {}, {}, {}, {}, {}, \
        {}, {}, {}, {}, {}, {}, {}, {}, {}, {},{}, {}, {}, {}, {}, {}, {}, '{}')""".format(d[0], d[1], d[2], d[3], d[4], d[5], d[6], \
        d[7], d[8], d[9], d[10], d[11], d[12], d[13], d[14], d[15], d[16], d[17], d[18], d[19], d[20], d[21], d[22], d[23],\
        d[24],d[25],d[26],d[27],','.join(d[28]))
        cursor.execute(insert)
        db.commit()
        cursor.execute("select * from gprs")
        data = cursor.fetchall()
        f.close()
    except struct.error:
        print("Пакет не полный. Записан его исходный вариант")


    