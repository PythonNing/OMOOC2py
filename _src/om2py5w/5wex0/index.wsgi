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

def read_diary_all():#	diarylog = open('diary log.txt','a+').read()#	return f.read()
	log = []
	diarylog = ""
	for i in list(kv.get_by_prefix("key")):
		log.append(i[1]) # i is type tuple with key-value
		temp = "%s\n TAG:%s\n%s\n\n" %(i[1]['time'],i[1]['tags'],i[1]['diary'])
		#temp = "%s\n%s\n%s\n" %(i[1]['time'],i[1]['diary'],i[1]['tag'])
		#temp = i[1]['tags']
		diarylog = diarylog + temp
		#i[1]['time']+"\n"+i[1]['diary']+"\n"+i[1]['tag']+"\n"
	#for j in range(count-1):
	#	print log[j]['time'], log[j]['diary']
	return log, diarylog

def write_diary(newdiary,tags,count):
	# key must be str()
	countkey = "key" + str(count)
	edit_time = strftime("%Y %b %d %H:%M:%S", localtime())
	diary = {'time':edit_time,'diary':newdiary,'tags':tags}
	kv.set(countkey,diary)

#	f = open('diary log.txt','a+')
#	f.write('%s    %s\n' % (edit_time, newdiary))
#	f.close()
#count = write_diary("hello world")
#count = write_diary("hello world again",count)
#print read_diary_all()
#write_diary("hello world 2","hh2")
#print read_diary_bykey(str(2))
#print read_diary("taghh2")



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
kv.disconnect_all()
