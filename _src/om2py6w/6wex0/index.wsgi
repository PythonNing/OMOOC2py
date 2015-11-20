# -*- coding: utf-8 -*-
#!/usr/bin/env python
# author: bambooom
'''
MyDiary Web Application
Open web browser and access http://omoocpy.sinaapp.com/
You can read the old diary and input new diary
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from bottle import Bottle, request, route, run, template
import sae
import sae.kvdb
from time import localtime, strftime
import hashlib
import urllib2
import xml.etree.ElementTree as ET

app = Bottle()
kv = sae.kvdb.Client()

@app.route('/wechat')
def check_signature():
	'''
	wechat access verification
	'''
	token = "bambooom2bpythonic"
	signature = request.GET.get('signature',None)
	timestamp = request.GET.get('timestamp',None)
	nonce = request.GET.get('nonce',None)
	echostr = request.GET.get('echostr',None)
	L = [token,timestamp,nonce]
	L.sort()
	s=L[0]+L[1]+L[2]
	if hashlib.sha1(s).hexdigest() == signature:
		return echostr
	else:
		return None

def parse_xml_msg(recv_xml):
	#recv_xml = request.body.read()
	root = ET.fromstring(recv_xml)
	msg = {}
	for child in root:
		msg[child.tag] = child.text
	return msg

recv_xml='''
<xml>
 <ToUserName><![CDATA[bambooom]]></ToUserName>
 <FromUserName><![CDATA[omoocpy]]></FromUserName> 
 <CreateTime>20151120</CreateTime>
 <MsgType><![CDATA[text]]></MsgType>
 <Content><![CDATA[WTF]]></Content>
 <MsgId>hdsicwecewew2233333</MsgId>
 </xml>
 '''

print type(parse_xml_msg(recv_xml))


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

#application = sae.create_wsgi_app(app)
