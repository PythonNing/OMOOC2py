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
log = []

def read_diary_bykey(count):
#	f = open('diary log.txt','a+')
#	return f.read()
	log.append(kv.get(count))
	return log

def write_diary(newdiary,count):
	# key must be str()
	count = str(count)
	edit_time = strftime("%Y %b %d %H:%M:%S", localtime())
	diary = {'time':edit_time, 'diary':newdiary}
	kv.set(count,diary)
#	f = open('diary log.txt','a+')
	
#	f.write('%s    %s\n' % (edit_time, newdiary))
#	f.close()
write_diary("hello world",1)
write_diary("hello world again",2)
#write_diary("hello world 2","hh2")
print read_diary_bykey(str(1))
print read_diary_bykey(str(2))
#print read_diary("taghh2")



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