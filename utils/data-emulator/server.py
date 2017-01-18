from socket import *
import params
import sys

Parser = params.Parser()
argv = Parser.createParser()
ip_and_port = argv.parse_args(sys.argv[1:])
host = ip_and_port.ip
port = int(ip_and_port.port)
addr = (host, port)

tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.bind(addr)
tcp_socket.listen(1)

while True:
    print('wait connection...')
    conn, addr = tcp_socket.accept()

    while True:
        print('client addr: ', addr)
        data = conn.recv(50000)
        print(data)
        if not data:
            break
conn.close()
tcp_socket.close()
