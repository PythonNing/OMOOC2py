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
import re

HELP = '''
Input h/help/? for help.
Input q/quit to quit the process.
Input s/sync to sync the diary log.
Input lt/ListTags to list all tags.
Input st:TAG to set or delete tags
Input FLUSH to clear all diary entries.
'''

def get_log():
	response = requests.get("http://bambooomhelloworld.sinaapp.com/")
	soup = BeautifulSoup(response.text, "html.parser")
	tag = soup.textarea
	return tag.string

def get_tags():
	diarylog = get_log()
	tags_all = re.findall(r'TAG:.*?\n',diarylog,re.DOTALL)
	tags = []
	for i in tags_all:
		temp = re.sub(r'TAG:','',i)
		tags.append(re.sub(r'\n','',temp))
	tags = list(set(tags))
	for i in tags:
		print i

#	html_code = response.read()
#	response.close()
#	text_area = re.findall(r'<textarea .*>.*</textarea>', html_code, re.DOTALL)
	# re.DOTALL make '.' can also represent newline
#	log = re.sub(r'<.*?>', '', text_area[0])
	# delete html tags
#	return log

def write_log(message, tags=''):
	values = {'newdiary':message,'tags':tags}
	response = requests.post("http://bambooomhelloworld.sinaapp.com/", data=values)
#	data = urllib.urlencode(values)
#	req = urllib2.Request("http://localhost:8255/mydiary", data) # post data
#	response = urllib2.urlopen(req)
#	response.close()

def client():

#	get_log()
#	write_log("aaaa","bbbb")

	while True:
		message = raw_input(' Input here>')
		if message in ['h','help','?']:
			print HELP
		elif message in ['s','sync']:
			print get_log()
		elif message in ['q','quit']:
			print 'Bye~'
			break
		elif message in ['lt','ListTags']:
			get_tags()


if __name__ == '__main__':
	client()
