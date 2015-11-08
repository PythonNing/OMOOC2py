# -*- coding: utf-8 -*- 
# author: bambooom
'''
My Diary Web Application - CLI for client
'''  
#import socket
#import sys
#from bottle import request, route, template

h = ['h','help','?']
q = ['q','quit']
r = ['r','sync']

import urllib2
import re
content=urllib2.urlopen("http://localhost:8255/mydiary")
print "http header:",content.info()
print "http status:",content.getcode()
print "url:",content.geturl()
log = content.read()
text = re.findall(r'<textarea .*>.*</textarea>', log, re.DOTALL)
text2 = text[0]
#tag = re.findall(r'<.*?>', text2, re.DOTALL)
#print text2
text3 = re.sub(r'<.*?>', '', text2)
print text3

#s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server_address = ('localhost/mydiary', 8255)
#s.connect(server_address)

#message = "GET / HTTP/1.1\r\n\r\n"

#s.sendall(message)

#reply = s.recv(4096)

#print reply

#s.sendto('r', server_address) # ask server to send the latest log
#log, server = s.recvfrom(4096)
#print log

#while True:
#	message = raw_input(' Input here>') # ask for input
	
#	if message in h:
#		print """ 
#		Input h/help/? for help.
#		Input q/quit to quit the process.
#		Input r/sync to sync the diary log
#		""" # print the help
#	elif message in r: # for request, contact server to send back the log
#		s.sendto(message, server_address) # client has to send the request for sync first
#		log, server = s.recvfrom(4096) # so that client can get the reply
#		print log
#	elif message in q:
#		print >>sys.stderr, 'Bye~'
#		break
#	else:
#		s.sendto(message, server_address)

s.close()
