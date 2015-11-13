# -*- coding: utf-8 -*-
#!/usr/bin/env python
# author: bambooom
'''
MyDiary Web Application
Open web browser and access http://bambooomdiary.sinaapp.com/
You can read the old diary and input new diary
'''

from bottle import Bottle, request, route, run, template
import sae
from time import localtime, strftime

def read_diary():
	f = open('diary log.txt','a+')
	return f.read()

def write_diary(newdiary):
	f = open('diary log.txt','a+')
	edit_time = strftime("%Y %b %d %H:%M:%S", localtime())
	f.write('%s    %s\n' % (edit_time, newdiary))
	f.close()

app = Bottle()

@app.route('/')
def start():
	log = read_diary()
	return template("diarysae", diarylog=log)

@app.route('/', method='POST')
def input_new():
	newdiary = request.forms.get('newdiary')
	write_diary(newdiary)
	log = read_diary()
	return template("diarysae", diarylog=log)

application = sae.create_wsgi_app(app)