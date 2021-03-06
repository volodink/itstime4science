from socket import *
import params
import functools
import sys
import asyncio

def event_handler(loop, stop=False):
    print('Вызван обработчик события')
    if stop:
        print('Цикл останавливается')
        loop.stop()
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.call_later(1, event_handler, loop)
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
            print('wait connection...')
            conn, addr = tcp_socket.accept()
            data = conn.recv(89)
            print(data)
            if data:
                f.write(data)
            else:
                break
        loop.run_forever()
    finally:
        loop.close()
    f.close()
    conn.close()
    tcp_socket.close()
