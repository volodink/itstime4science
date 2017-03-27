import struct
f = open('/home/argo/PycharmProjects/untitled/gprs_packet.bin', 'rb')
SYT=f.read(3)
print(SYT)
def read_data(file):
    var = []
    var = file.read()
    return var
while (1) :
    if SYT == b'SYT':
        mas = []
        print("YAY!")
        mas = read_data(f)
        print(mas)
        for i in range(len(mas)):
            print(mas[i])
        print('----------')
        print(i)
        # print(time)
        # time+=1
        # print(time)
        break
else: print("All baaaad, i will try again (∘⌢∘)")

# ГЛЯНУТЬ ЕМЕТ
# time = do_while(f, 4)
# lat = do_while(f, 4)
# lon = do_while(f, 4)
# alt = do_while(f, 4)
# temp1 = do_while(f, 4)
# temp2 = do_while(f, 4)
# pressure1 = do_while(f, 4)
# pressure2 = do_while(f, 4)
# bat_crg = do_while(f, 1)
# bat_volt = do_while(f, 4)
# bat_temp = do_while(f, 4)
# vect_axel1 = do_while(f, 4)
# vect_axel2 = do_while(f, 4)
# ultraviolet1 = do_while(f, 4)
# ultraviolet2 = do_while(f, 4)
# infrared1 = do_while(f, 4)
# infrared2 = do_while(f, 4)
# hdop = do_while(f, 4)
# vdop = do_while(f, 4)
# sats = do_while(f, 1)
# radiation = do_while(f, 4)
# dust = do_while(f, 4)
# ozone = do_while(f, 1)
# stop = do_while(f, 3)