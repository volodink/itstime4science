from socket import *
from modules import decode_packet
import sys
from modules import params

Parser = params.Parser()
argv = Parser.createParser()
ip_and_port = argv.parse_args(sys.argv[1:])
#host = ip_and_port.ip
#port = int(ip_and_port.port)
host = "0.0.0.0"
port = 5300
addr = (host, port)
print(host,port)
tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.bind(addr)
tcp_socket.listen(10)
loop = True
while loop:
    data = None
    print('wait connection...')
    conn, addr = tcp_socket.accept()
    while loop:
        f = open('logs/gprs.log', 'a+')
        data = conn.recv(109)
        decode_packet.insert(data)
        print(data)
        if data:
            f.write(str(data))
            f.close()
        else:
            f.close()
            break
conn.close()
tcp_socket.close()
