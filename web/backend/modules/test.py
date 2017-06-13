import time
import aprslib

def callback(packet):
    packet = packet.decode('utf-8')
    new = packet.split("# aprsc")
    tm = time.localtime()
    print(time.strftime("%Y%m%d%H%M%S", tm))
    if type(new) != list:
        print(packet)
        buf = packet.split("UB4FEU-11>UB4FEU,R4FBA-1*,WIDE1*,WIDE2-2,qAR,RA4FHE-1:T#")
        buf = buf.split(',')

AIS = aprslib.IS("UB4FEU", passwd="22451", port=14580)
AIS.set_filter("b/UB4FEU-11")
AIS.connect()
AIS.consumer(callback, raw=True)
