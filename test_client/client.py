from socket import *
import sys
from dataemulator import telemetrySenderEmulator
import time
import params

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
file = open("binary.file", "rb")
while not file.eof:
    buff = file.read(89)  # считать 1024 байт
    string = base64.b64encode(buff)  # base64 кодирование
    buff = str.encode(buff) # Вот это под вопросом, перед этим вместо buff  на обоих местах стояла data
    tcp_socket.send(file)
    print('Data has been sent')

tcp_socket.close()
