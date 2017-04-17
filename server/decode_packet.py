from datetime import datetime
import struct
import MySQLdb

f = open('packet.bin', 'rb')
SYT=f.read(3)
print(SYT)
def packet(*args,i):
    return args[i]

def clear_string(str):
    new_str = ''
    for s in str:
        return s
def str_to_float(str):
    # попробуем воспользоваться самым простым методом
    try:
        return float(str)
    except:
        # других вариантов не осталось. скорее всего функция приняла на входе мусор
        return 0

def check_float(str):
    try:
        float(str)
        return True
    except:
        return False

def read_data(file,n):
    var = []
    var = file.read(n)
    return var

def toBitArray(val, maxBitCount=23):
    return list(map(lambda x: 'false' if (x == '0') else 'ok', '{0:023b}'.format(val)))

def run(number):
    print(*toBitArray(number))
    print(len(toBitArray(number)))
    return toBitArray(number)

i=0
d = [] #time

data = 10001
d.append(data)

data = read_data(f, 4)#time
data =int.from_bytes(data, byteorder='little')
print(datetime.fromtimestamp(data))
data = datetime.fromtimestamp(data)
print(str(data))
data = str(data)
d.append(data)


data = read_data(f, 4) #lat
data = struct.unpack('f',data)
d.append (clear_string(data))

data = read_data(f, 4) #lon
data = struct.unpack('f',data)
d.append (clear_string(data))


data = read_data(f, 4) #alt
data = struct.unpack('f',data)
d.append (clear_string(data))


data = read_data(f, 4)#temp1
data = struct.unpack('f',data)
d.append (clear_string(data))

data = read_data(f, 4)#temp2
data = struct.unpack('f',data)
d.append (clear_string(data))


data = read_data(f, 4)#pressure1
data= struct.unpack('f',data)
d.append (clear_string(data))

data = read_data(f, 4)#pressure2
data= struct.unpack('f',data)
d.append (clear_string(data))

data = read_data(f, 1)#bat_crg
d.append (int.from_bytes(data, byteorder='little'))

data = read_data(f, 4)#bat_volt
data= struct.unpack('f',data)
d.append (clear_string(data))


data = read_data(f, 4)#bat_temp
data= struct.unpack('f',data)
d.append (clear_string(data))

data = read_data(f, 4)#vect_axel1
data= struct.unpack('f',data)
d.append (clear_string(data))

data = read_data(f, 4)#vect_axel2
data= struct.unpack('f',data)
d.append (clear_string(data))

data = read_data(f, 4)#ultraviolet1
data= struct.unpack('f',data)
d.append (clear_string(data))

data = read_data(f, 4)#ultraviolet2
data= struct.unpack('f',data)
d.append (clear_string(data))

data = read_data(f, 4)#infrared1
data= struct.unpack('f',data)
d.append (clear_string(data))

data = read_data(f, 4)#infrared2
data = struct.unpack('f',data)
d.append (clear_string(data))


data = read_data(f, 4)#hdop
data = struct.unpack('f',data)
d.append (clear_string(data))


data = read_data(f, 4)#vdop
data= struct.unpack('f',data)
d.append (clear_string(data))

data = read_data(f, 1)#sats
d.append(int.from_bytes(data, byteorder='little'))

data = read_data(f, 4)#radiation
data= struct.unpack('f',data)
d.append (clear_string(data))

data = read_data(f, 4)#dust
data= struct.unpack('f',data)
d.append (clear_string(data))

data = read_data(f, 1)#ozone
d.append(bool(data))

data = read_data(f, 4)#status
databin = int.from_bytes(data, byteorder='little')
l = run(databin)
d.append(l)



f = open('formated_dates.txt', 'w')
print(d[0:24])
for i in range(len(d)):
    f.write(str(d[i]) + '    ')
db = MySQLdb.connect(host="localhost", user="root", passwd="s21021999s", db="packet", charset='utf8')
cursor = db.cursor()
try:
    insert ="""INSERT INTO gprs(numbersOfFlight, datatime, lat, lon,alt,temp1,temp2,pressure1,pressure2,bat_crg,\
bat_volt,bat_temp,vect_axel1,vect_axel2,ultraviolet1,ultraviolet2,infrared1,infrared2,hdop,vdop,sats,radiation,\
dust,ozone,status) VALUES({}, '{}', {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, '{}')""".format(d[0], d[1], d[2], d[3], d[4], d[5], d[6], d[7], d[8], d[9], d[10], d[11], d[12], d[13], d[14], d[15], d[16],\
 d[17], d[18], d[19], d[20], d[21], d[22], d[23], ','.join(d[24]))

    #insert = "i i oooo v ({},{},{})".format(10,20,30)
    print(insert)
    cursor.execute(insert)
    db.commit()
    cursor.execute("select * from gprs")
    data = cursor.fetchall()
    print (data)
except MySQLdb.Error as e:
    print ("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
else:
    db.close()


# except:
#     db.rollback()

#data =  cursor.fetchall()
# # ГЛЯНУТЬ ЕМЕТ
#d[0], d[1], d[2], d[3], d[4], d[5], d[6], d[7], d[8], d[9], d[10], d[11], d[12], d[13], d[14], d[15], d[16], d[17], d[18], d[19], d[20], d[21], d[22], d[23], d[24]
#%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s