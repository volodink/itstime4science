import struct

f = open('packet.bin', 'rb')
SYT=f.read(3)
print(SYT)
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


d = [] #time

data = read_data(f, 4)#time
data =int.from_bytes(data, byteorder='little')
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
print(bool(data))
d.append(bool(data))

data = read_data(f, 4)#status
databin = int.from_bytes(data, byteorder='little')
l = run(databin)
d.append(l)


f = open('formated_dates.txt', 'w')
print(d[0:24])
for i in range(len(d)):
    f.write(str(d[i]) + '    ')
f.close()
# # ГЛЯНУТЬ ЕМЕТ
