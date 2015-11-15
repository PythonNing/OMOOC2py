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
url = "http://bambooomhelloworld.sinaapp.com/"

def get_log_all():
	response = requests.get(url)
	soup = BeautifulSoup(response.text, "html.parser")
	tag = soup.textarea
	return tag.string

def get_log_bytag(tags):
	response = requests.get(url)
	soup = BeautifulSoup(response.text, "html.parser")
	tag = soup.textarea
	log = ''
	if not tag.string:
		pass
	else:
		temp = tag.string.splitlines()
		for i in range(len(temp)):
			if temp[i] == ' TAG:'+tags:
				log += temp[i-1]+'\n'+temp[i+1]+'\n'
			else:
				pass
	return log

def get_tags():
	diarylog = get_log_all()
	if not diarylog:
		pass
	else:
		tags_all = re.findall(r'TAG:.*?\n',diarylog,re.DOTALL)
		tags = []
		for i in tags_all:
			temp = re.sub(r'TAG:','',i)
			tags.append(re.sub(r'\n','',temp))
		tags = list(set(tags))
		for i in tags:
			print i

def delete_log():
	res = raw_input('ARE YOU SURE?(y/n)>')
	if res.lower() == 'y':
#		response = requests.delete(url)
		response = requests.get(url+'delete')
		print "All clear!Restart a new diary!"
	else:
		print "Well, keep going on!"

def write_log(message, tags):
	values = {'newdiary':message,'tags':tags}
	response = requests.post(url, data=values)


def client():

	print HELP 
	tags=''

	while True:
		print 'TAG:'+tags
		message = raw_input('Input>')
		if message in ['h','help','?']:
			print HELP
		elif message in ['s','sync']:
			print get_log_bytag(tags)
		elif message in ['q','quit']:
			print 'Bye~'
			break
		elif message in ['lt','ListTags']:
			get_tags()
		elif message.startswith('st:'):
			tags = message[3:]
		elif message == 'FLUSH':
			delete_log()
		else:
			write_log(message,tags)


if __name__ == '__main__':
	client()
