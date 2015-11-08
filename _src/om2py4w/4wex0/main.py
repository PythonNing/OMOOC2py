# -*- coding: utf-8 -*-
#!/usr/bin/env python
# author: bambooom
'''
MyDiary Web Application
Open web browser and access http://localhost:8255/mydiary
You can read the old diary and input new diary
'''

from bottle import request, route, run, template
from time import localtime, strftime

def read_diary():
	f = open('diary log.txt','a+')
	return f.read()

def write_diary(newdiary):
	f = open('diary log.txt','a+')
	edit_time = strftime("%Y %b %d %H:%M:%S", localtime())
	f.write('%s    %s\n' % (edit_time, newdiary))
	f.close()

@route('/mydiary')
def start():
	log = read_diary()
	return template("diaryweb", diarylog=log)

@route('/mydiary', method='POST')
def input_new():
	newdiary = request.forms.get('newdiary')
	write_diary(newdiary)
	log = read_diary()
	return template("diaryweb", diarylog=log)


if __name__ == '__main__':
	run(host='localhost', port=8255, debug=True, reloader=True)
	
