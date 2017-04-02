from socket import *
import params
import sys
import asyncio

Parser = params.Parser()
argv = Parser.createParser()
ip_and_port = argv.parse_args(sys.argv[1:])
#host = ip_and_port.ip
#port = int(ip_and_port.port)
event_loop = asyncio.get_event_loop()
f = open('packet.bin', 'wb')
tcp_socket = socket(AF_INET, SOCK_STREAM)



host = "0.0.0.0"
port = 5100
addr = (host, port)
print(host,port)
tcp_socket.bind(addr)
tcp_socket.listen(1)
print('wait connection...')
conn, addr = tcp_socket.accept()
data = conn.recv(89)
async def write(data):
    f.write(data)
async def main():
    await asyncio.wait(write(data))
try:
    asyncio.ensure_future(write(data))
    event_loop.run_forever()
finally:
    event_loop.close()
    f.close()
    tcp_socket.close()
