# -*- coding: utf-8 -*- 
# author: bambooom
'''
My Diary Web App - CLI for client
'''  
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import requests
from bs4 import BeautifulSoup



def get_log():
	response = requests.get("http://bambooomhelloworld.sinaapp.com/")
	soup = BeautifulSoup(response.text, "html.parser")
	tag = soup.textarea
	print tag.string
#	html_code = response.read()
#	response.close()
#	text_area = re.findall(r'<textarea .*>.*</textarea>', html_code, re.DOTALL)
	# re.DOTALL make '.' can also represent newline
#	log = re.sub(r'<.*?>', '', text_area[0])
	# delete html tags
#	return log

#def write_log(message):
#	values = {'newdiary' : message}
#	data = urllib.urlencode(values)
#	req = urllib2.Request("http://localhost:8255/mydiary", data) # post data
#	response = urllib2.urlopen(req)
#	response.close()

def client():
	h = ['h','help','?']
	q = ['q','quit']
	r = ['r','sync']
	
	get_log()

	#while True:
	#	message = raw_input(' Input here>')
	#	if message in h:
	#		print """ 
	#		Input h/help/? for help.
	#		Input q/quit to quit the process.
	#		Input r/sync to sync the diary log
	#		"""
	#	elif message in r:
	#		print get_log()
	#	elif message in q:
	#		print 'Bye~'
	#		break
	#	else:
	#		write_log(message)


if __name__ == '__main__':
	client()
