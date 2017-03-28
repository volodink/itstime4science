from socket import *
import sys
from dataemulator import telemetrySenderEmulator
import time
import params
import string
import base64

Parser = params.Parser()
gen = telemetrySenderEmulator.generateData()
argv = Parser.createParser()
ip_and_port = argv.parse_args(sys.argv[1:])
#host = ip_and_port.ip
#port = int(ip_and_port.port)
host = "0.0.0.0"
port = 5100
print(host,port)

addr = (host, port)
tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.connect(addr)
file = open("generate_packet/gprs_packet.bin", "rb")
while True:
    buf = file.read()

    if len(buf) == 0:
        break
    print(buf)
    tcp_socket.send(buf)
    print ('Data has been sent')
file.close() 
tcp_socket.close()
