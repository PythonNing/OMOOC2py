# -*- coding: utf-8 -*- 
# ----------3w task:MyDiaryNet CLI----------
# -------------author: bambooom-------------  

# Echo client program
import socket
import sys

# create socket of client to contact the server
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 8250)

h = ['h','help','?']
q = ['q','quit']
r = ['r','sync']

s.sendto('r', server_address) # ask server to send the latest log
log, server = s.recvfrom(4096)
print log

while True:
	message = raw_input(' Input here>') # ask for input
	
	if message in h:
		print """ 
		Input h/help/? for help.
		Input q/quit to quit the process.
		Input r/sync to sync the diary log
		""" # print the help
	elif message in r: # for request, contact server to send back the log
		s.sendto(message, server_address) # client has to send the request for sync first
		log, server = s.recvfrom(4096) # so that client can get the reply
		print log
	elif message in q:
		print >>sys.stderr, 'Bye~'
		break
	else:
		s.sendto(message, server_address)

s.close()
