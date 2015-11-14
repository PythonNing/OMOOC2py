# -*- coding: utf-8 -*-
#!/usr/bin/env python
# author: bambooom
'''
MyDiary Web Application
Open web browser and access http://bambooomhelloworld.sinaapp.com/
You can read the old diary and input new diary
'''

from bottle import Bottle, request, route, run, template
import sae
import sae.kvdb
from time import localtime, strftime

app = Bottle()
kv = sae.kvdb.Client()

def read_diary_all():
	log = []
	diarylog = ""
	for i in list(kv.get_by_prefix("key")):
		log.append(i[1])
		temp = "%s\n TAG:%s\n%s\n\n" %(i[1]['time'],i[1]['tags'],i[1]['diary'])
		diarylog = diarylog + temp
	return log, diarylog

def write_diary(newdiary,tags,count):
	# key must be str()
	countkey = "key" + str(count)
	edit_time = strftime("%Y %b %d %H:%M:%S", localtime())
	diary = {'time':edit_time,'diary':newdiary,'tags':tags}
	kv.set(countkey,diary)

@app.route('/')
def start():
	diarylog = read_diary_all()[1]
	return template("diarysae", diarylog=diarylog)

@app.route('/', method='POST')
def input_new():
	count = len(read_diary_all()[0])
	newdiary = request.forms.get('newdiary')
	tags = request.forms.get('tags')
	write_diary(newdiary,tags,count)
	diarylog = read_diary_all()[1]
	return template("diarysae", diarylog=diarylog)

application = sae.create_wsgi_app(app)
