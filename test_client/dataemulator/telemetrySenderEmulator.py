#!/usr/bin/env python3.5

import random
import time
import socket
import sys
class generateData():
	
	def __init__(self):
		pass

	def getMessage(self):

		message = "SYT,{0},{1},{2},{3},{4},{5},{6},TYS"
		return message.format(time.time(),
							random.uniform(0.0, 360.0),
							random.uniform(0.0, 360.0),
							random.uniform(0.0, 30.0),
							random.uniform(-60.0, 60.0),
							random.uniform(-60.0, 60.0),
							random.uniform(-100.0, 100.0))

	def sortMessage(self, message):

		template = """
		--------------------------------------
		Time stamp: %f;
		Lat: %f;
		Lon: %f;
		Alt: %f;
		t1: %f;
		t2: %f;
		P: %f;
		--------------------------------------
		""" 

		dataList = [float(i) for i in message.split(",")[1:8]]
		print(template % tuple(dataList))
		time.sleep(1)

class startServer():

	def __init__(self, ip, port):

		self.sock = socket.socket()
		try:
			self.sock.connect((ip, port))
		except ConnectionRefusedError:
			print("Дебил, где сервер?")
			sys.exit(0)


	def __del__(self):

		self.sock.close()

	def sendMessage(self, message):


		while True:
			try:
				print(message)
				self.sock.send(bytes(message))
				time.sleep(0.5)	
			except KeyboardInterrupt:
				break 	





if __name__ == "__main__":

	server = startServer("127.0.0.1", 8080)
	gen = generateData()
	server.sendMessage(gen.getMessage())
	

	# printMessage(getMessage)
	# gen = generateData()

	# while True:
	# 	gen.sortMessage(gen.getMessage())
