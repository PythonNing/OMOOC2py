# -*- coding: utf-8 -*-
#!/usr/bin/env python
# author: bambooom
'''
MyDiary Web Application
Open web browser and access http://bambooomhelloworld.sinaapp.com/
You can read the old diary and input new diary
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from bottle import Bottle, request, route, run, template
import sae
import sae.kvdb
from time import localtime, strftime

app = Bottle()
kv = sae.kvdb.Client()

def read_diary_all():
	log = []
	for i in list(kv.get_by_prefix("key#")):
		log.append(i[1])
	return log

def write_diary(newdiary,tags,count):
	# key must be str()
	countkey = "key#" + str(count)
	edit_time = strftime("%Y %b %d %H:%M:%S", localtime())
	diary = {'time':edit_time,'diary':newdiary,'tags':tags}
	kv.set(countkey,diary)

@app.route('/')
def start():
	diarylog = read_diary_all()
	return template("diarysae", diarylog=diarylog)

@app.route('/', method='POST')
def input_new():
	count = len(read_diary_all())
	newdiary = unicode(request.forms.get('newdiary'),'utf-8')
	tags = unicode(request.forms.get('tags'),'utf-8')
	write_diary(newdiary,tags,count)
	diarylog = read_diary_all()
	return template("diarysae", diarylog=diarylog)

@app.route('/', method='DELETE')
def delete():
	temp = kv.getkeys_by_prefix("key#")
	for i in temp:
		kv.delete(i)

application = sae.create_wsgi_app(app)
