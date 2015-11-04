# !/usr/bin/env python
# -*- coding: utf-8 -*- 
# ----------3w task:MyDiaryNet CLI----------
# -------------author: bambooom-------------  

# Echo server program
import socket
import sys
from time import localtime, strftime

# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind the socket to the port
server_address = ('localhost', 8250)
print >>sys.stderr, 'starting up on %s port %s' % server_address
s.bind(server_address)

f = open('diary log.txt','a+')
print f.read()  #print log

h = ['h','help','?']
q = ['q','quit']
r = ['r','sync']

while True:
	data, address = s.recvfrom(4096) # loop to receive from client
	
	if data in q or data in h:
		pass
	elif data in r: # client request to sync the log
		f = open('diary log.txt','r')
		log = f.read()
		s.sendto(log, address) # so send back log to the client
	elif data not in set(q)|set(h)|set(r):
		f = open('diary log.txt','a+')
		edit_time = strftime("%a, %Y %b %d %H:%M:%%S", localtime()) # 
		f.write("%s From %s:  %s\n" % (edit_time, address, data)) 
		# write input into local file
		# with address and time
		f.close()
		print >>sys.stderr, data
	elif not data:
		break

s.close()
