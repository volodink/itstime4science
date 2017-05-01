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
port = 5100
addr = (host, port)
print(host,port)
tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.bind(addr)
tcp_socket.listen(1)
f = open('packet.bin', 'wb')
while True:
    # tcp_socket.settimeout(5)
    print('wait connection...')
    conn, addr = tcp_socket.accept()
    data = conn.recv(109)
    decode_packet.insert(data)
    print(data)
    if data:
        f.write(data)
    else:
        break

f.close()
conn.close()
tcp_socket.close()

# from socket import *
# import params
# import decode_packet
# import sys
# import asyncio
#
# def event_handler(loop, stop=False):
#     print('Вызван обработчик события')
#     if stop:
#         print('Цикл останавливается')
#         loop.stop()
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     try:
#         loop.call_later(1, event_handler, loop)
#         Parser = params.Parser()
#         argv = Parser.createParser()
#         ip_and_port = argv.parse_args(sys.argv[1:])
#         #host = ip_and_port.ip
#         #port = int(ip_and_port.port)
#         host = "localhost"
#         port = 5100
#         addr = (host, port)
#         print(host,port)
#         tcp_socket = socket(AF_INET, SOCK_STREAM)
#         tcp_socket.bind(addr)
#         tcp_socket.listen(1)
#         f = open('packet.bin', 'rb')
#         while True:
#             print('wait connection...')
#             conn, addr = tcp_socket.accept()
#             data = conn.recv(109)
#             print(data)
#             f.write(data)
#             f.close()
#             conn.close()
#
#         loop.run_forever()
#     finally:
#         loop.close()
#         tcp_socket.close()

