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
import sae.kvdb
from time import localtime, strftime

app = Bottle()
kv = sae.kvdb.Client()

def read_diary():
#	f = open('diary log.txt','a+')
#	return f.read()
	pass

def write_diary(newdiary,tag):
	edit_time = strftime("%Y %b %d %H:%M:%S", localtime())
	tag = "tag" + tag
	diary = {'time':edit_time, 'diary':newdiary}
	kv.add(tag,newdiary)
	return diary
#	f = open('diary log.txt','a+')
	
#	f.write('%s    %s\n' % (edit_time, newdiary))
#	f.close()

print write_diary("hello world","hh")


#@app.route('/')
#def start():
#	log = read_diary()
#	return template("diarysae", diarylog=log)

#@app.route('/', method='POST')
#def input_new():
#	newdiary = request.forms.get('newdiary')
#	write_diary(newdiary)
#	log = read_diary()
#	return template("diarysae", diarylog=log)

#application = sae.create_wsgi_app(app)