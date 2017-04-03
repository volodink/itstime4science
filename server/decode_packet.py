import struct
f = open('packet.bin', 'rb')
SYT=f.read(3)
print(SYT)
def read_data(file,n):
    var = []
    var = file.read(n)
    return var
time = read_data(f, 4)
time =int.from_bytes(time, byteorder='little')
print(time)

lat = read_data(f, 4)
lat = struct.unpack('f',lat)
print(lat)

lon = read_data(f, 4)
lon = struct.unpack('f',lon)
print(lon)

alt = read_data(f, 4)
alt = struct.unpack('f',alt)
print(alt)

temp1 = read_data(f, 4)
temp1 = struct.unpack('f',temp1)
print(temp1)

temp2 = read_data(f, 4)
temp2 = struct.unpack('f',temp2)
print(temp2)

pressure1 = read_data(f, 4)
pressure1= struct.unpack('f',pressure1)
print(pressure1)

pressure2 = read_data(f, 4)
pressure2= struct.unpack('f',pressure2)
print(pressure2)

bat_crg = read_data(f, 1)
bat_crg = int.from_bytes(bat_crg, byteorder='little')
print(bat_crg)

bat_volt = read_data(f, 4)
bat_volt= struct.unpack('f',bat_volt)
print(bat_volt)

bat_temp = read_data(f, 4)
bat_temp= struct.unpack('f',bat_temp)
print(bat_temp)

vect_axel1 = read_data(f, 4)
vect_axel1= struct.unpack('f',vect_axel1)
print(vect_axel1)

vect_axel2 = read_data(f, 4)
vect_axel2= struct.unpack('f',vect_axel2)
print(vect_axel2)

ultraviolet1 = read_data(f, 4)
ultraviolet1= struct.unpack('f',ultraviolet1)
print(ultraviolet1)

ultraviolet2 = read_data(f, 4)
ultraviolet2= struct.unpack('f',ultraviolet2)
print(ultraviolet2)

infrared1 = read_data(f, 4)
infrared1= struct.unpack('f',infrared1)
print(infrared1)

infrared2 = read_data(f, 4)
infrared2= struct.unpack('f',infrared2)
print(infrared2)

hdop = read_data(f, 4)
hdop= struct.unpack('f',hdop)
print(hdop)

vdop = read_data(f, 4)
vdop= struct.unpack('f',vdop)
print(vdop)

sats = read_data(f, 1)
sats= int.from_bytes(sats, byteorder='little')
print(sats)

radiation = read_data(f, 4)
radiation= struct.unpack('f',radiation)
print(radiation)
dust = read_data(f, 4)
dust= struct.unpack('f',dust)
print(dust)
#ozone = read_data(f, 1)

stop = read_data(f, 3)

# ГЛЯНУТЬ ЕМЕТ
