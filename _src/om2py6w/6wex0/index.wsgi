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

#@app.route('/wechat')
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

def parse_xml_msg():
	recv_xml = request.body.read()
	root = ET.fromstring(recv_xml)
	msg = {}
	for child in root:
		msg[child.tag] = child.text
	return msg

'''
server receiving data
<xml>
 <ToUserName><![CDATA[bambooom]]></ToUserName>
 <FromUserName><![CDATA[omoocpy]]></FromUserName> 
 <CreateTime>20151120</CreateTime>
 <MsgType><![CDATA[text]]></MsgType>
 <Content><![CDATA[WTF]]></Content>
 <MsgId>hdsicwecewew2233333</MsgId>
 </xml>
 '''

'''
server sending data
<xml>
<ToUserName><![CDATA[toUser]]></ToUserName>
<FromUserName><![CDATA[fromUser]]></FromUserName>
<CreateTime>12345678</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[你好]]></Content>
</xml>
'''
#print type(parse_xml_msg(recv_xml))


def read_diary_all():
	log = []
	for i in list(kv.get_by_prefix("key#")):
		log.append(i[1])
	return log

def write_diary(newdiary,count):
	# key must be str()
	countkey = "key#" + str(count)
	edit_time = strftime("%Y %b %d %H:%M:%S", localtime())
	diary = {'time':edit_time,'diary':newdiary}
	kv.set(countkey,diary)

#@app.route('/')
#def start():
#	diarylog = read_diary_all()
#	return template("diarysae", diarylog=diarylog)

@app.route('/')
def response_wechat():
	'''
	response in wechat platform
	'''
	#msg = parse_xml_msg()
	msg={'FromUserName': 'omoocpy', 'MsgId': 'hdsicwecewew2233333', 
	'ToUserName': 'bambooom', 'Content': 'diary WTF', 'MsgType': 'text', 
	'CreateTime': '20151120'}

	response_msg = '''
	<xml>
	<ToUserName><![CDATA[%s]]></ToUserName>
	<FromUserName><![CDATA[%s]]></FromUserName>
	<CreateTime>%s</CreateTime>
	<MsgType><![CDATA[text]]></MsgType>
	<Content><![CDATA[%s]]></Content>
	</xml>
	'''
	HELP = '''
	目前可使用的姿势:
	diary ~吐了个槽
	see   ~吐过的槽
	help  ~怎么吐槽

	'''
	if msg['Content'].startswith('diary'):
		newdiary = msg['Content'][5:]
		count = len(read_diary_all())
		write_diary(newdiary,count)
		echo_msg = response_msg % (
			msg['FromUserName'],msg['ToUserName'],strftime("%Y %b %d", localtime()),
			u"Got!"+str(count+1)+u"条吐槽啦!")
	#elif msg['Content'] == 'see'

	#	echo_msg = response_msg % (
	#		msg['FromUserName'],msg['ToUserName'],str(int(time.time())),HELP)
	return echo_msg



	#count = len(read_diary_all())
	#newdiary = unicode(request.forms.get('newdiary'),'utf-8')
	#tags = unicode(request.forms.get('tags'),'utf-8')
	#write_diary(newdiary,tags,count)
	#diarylog = read_diary_all()
	#return template("diarysae", diarylog=diarylog)

#@app.route('/', method='DELETE')
#def delete():
#	temp = kv.getkeys_by_prefix("key#")
#	for i in temp:
#		kv.delete(i)

application = sae.create_wsgi_app(app)
