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
url = "http://bambooomdiary.sinaapp.com/"

def get_log_all():
	response = requests.get(url)
	soup = BeautifulSoup(response.text, "html.parser")
	log = ''
	for i in soup.find_all('pre'):
		log += i.get_text()+'\n'
	return log

def get_log_bytag(tags):
	response = requests.get("http://bambooomhelloworld.sinaapp.com/")
	soup = BeautifulSoup(response.text,"html.parser")
	ti=list(soup.find_all('i', class_='etime'))
	ta=list(soup.find_all('i', class_='tags'))
	di=list(soup.find_all('pre',class_='diary'))
	for i in range(len(list(ti))):
		if ta[i].get_text() == 'TAG:'+tags:
			print "%s  %s" %(ti[i].get_text(),di[i].get_text())

def get_tags():
	response = requests.get(url)
	soup = BeautifulSoup(response.text, "html.parser")
	temp =[]
	for i in soup.find_all('i', class_='tags'):
		temp.append(i.get_text())
	tag_set = list(set(temp))
	for i in tag_set:
		print i

def delete_log():
	res = raw_input('ARE YOU SURE?(y/n)>')
	if res.lower() == 'y':
		response = requests.delete(url)
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
			get_log_bytag(tags)
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
