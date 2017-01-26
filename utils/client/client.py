from socket import *
import sys
import itstime4science.utils.dataemulator.telemetrySenderEmulator
import time
from itstime4science.params import params

Parser = params.Parser()
gen = telemetrySenderEmulator.generateData()
argv = Parser.createParser()
ip_and_port = argv.parse_args(sys.argv[1:])
host = ip_and_port.ip
port = int(ip_and_port.port)
addr = (host, port)
tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.connect(addr)

while(True):
    try:
        data = gen.getMessage()
        print("Gen data: ", data)
        if not data:
            tcp_socket.close()
            sys.exit(1)
        data = str.encode(data)
        tcp_socket.send(data)
        print(data)
        time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nCtr + C")
        tcp_socket.close()
        sys.exit(1)

tcp_socket.close()
