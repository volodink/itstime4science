from socket import *
from modules import decode_packet

tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.bind(('',5100))
tcp_socket.listen(50)
while True:
    print('Жду соединения')
    conn, addr = tcp_socket.accept()
    while True:
        f = open('logs/gprs.log', 'a+')
        data = conn.recv(109)
        print('Пакет получен, сохраняю')
        if data:
            decode_packet.insert(data)
            print('Исходные данные:' + str(data))
            f.write(str(data) + '\n')
            f.close()
        if not data:
            break
print('Connection is close')
conn.close()
tcp_socket.close()