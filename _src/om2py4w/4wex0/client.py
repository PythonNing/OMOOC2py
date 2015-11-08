# -*- coding: utf-8 -*- 
# author: bambooom
'''
My Diary Web Application - CLI for client
'''  
import urllib
import urllib2
import re

def get_log():
	response = urllib2.urlopen("http://localhost:8255/mydiary")
	html_code = response.read()
	response.close()
	text_area = re.findall(r'<textarea .*>.*</textarea>', html_code, re.DOTALL)
	log = re.sub(r'<.*?>', '', text_area[0])
	return log

def write_log(message):
	values = {'newdiary' : message}
	data = urllib.urlencode(values)
	req = urllib2.Request("http://localhost:8255/mydiary", data)
	response = urllib2.urlopen(req)
	response.close()

def client():
	h = ['h','help','?']
	q = ['q','quit']
	r = ['r','sync']
	
	print get_log()

	while True:
		message = raw_input(' Input here>')
		if message in h:
			print """ 
			Input h/help/? for help.
			Input q/quit to quit the process.
			Input r/sync to sync the diary log
			"""
		elif message in r:
			print get_log()
		elif message in q:
			print 'Bye~'
			break
		else:
			write_log(message)


if __name__ == '__main__':
	client()
