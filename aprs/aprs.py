import time
import aprslib
import pymysql
import os
import decode_aprs



AIS = aprslib.IS("NOCALL", port=14580)
AIS.set_filter("b/UB4FEU*")
AIS.connect()
AIS.consumer(decode_aprs.callback, raw=True)

# aprsc 2.1.4-g408ed49 14 Jun 2017 09:29:41 GMT NINTH 205.233.35.46:14580
# javAPRSSrvr 4.2.1b12 2017-06-16T20:09:26.369Z SEVENTH 14580
# UB4FEU-11>UB4FEU,R4FBA-1*,WIDE1*,WIDE2-2,qAR,RA4FHE-1:T#107,0.00,0.00,0.00,27.50,955.11,1111