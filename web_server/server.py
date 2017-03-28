from socket import *
import params
import sys

Parser = params.Parser()
argv = Parser.createParser()
ip_and_port = argv.parse_args(sys.argv[1:])
#host = ip_and_port.ip
#port = int(ip_and_port.port)
host = "0.0.0.0"
port = 5100
addr = (host, port)
print(host,port)
tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.bind(addr)
tcp_socket.listen(1)
f = open('packet.txt', 'wb')
while True:
    tcp_socket.settimeout(5)
    print('wait connection...')
    conn, addr = tcp_socket.accept()
    data = conn.recv(89)
    print(data)
    if data:
        f.write(data)
    else:
        break
f.close()
conn.close()
tcp_socket.close()
