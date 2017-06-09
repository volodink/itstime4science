import aprslib

def callback(packet):
    print (packet)
AIS = aprslib.IS("UB4FEU", port=14580)
AIS.set_filter("b/RA4FHE*")
AIS.connect()
AIS.consumer(callback)