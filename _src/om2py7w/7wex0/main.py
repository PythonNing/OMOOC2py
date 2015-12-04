# -*- coding: utf-8 -*- 
#qpy:MyDiary WebApp on Android
#qpy:2
#qpy:fullscreen
#qpy://127.0.0.1:8080/
"""
MyDiary WebApp on QPython
@Author bambooom
"""

from bottle import Bottle, ServerAdapter, run, route, request, template
import sqlite3
import time
from time import localtime, strftime
import xml.etree.ElementTree as ET
import requests
import os
#### 常量定义 #########
ROOT = os.path.dirname(os.path.abspath(__file__))


######### QPYTHON WEB SERVER ###############

class MyWSGIRefServer(ServerAdapter):
    server = None

    def run(self, handler):
        from wsgiref.simple_server import make_server, WSGIRequestHandler
        if self.quiet:
            class QuietHandler(WSGIRequestHandler):
                def log_request(*args, **kw): pass
            self.options['handler_class'] = QuietHandler
        self.server = make_server(self.host, self.port, handler, **self.options)
        self.server.serve_forever()

    def stop(self):
        #sys.stderr.close()
        import threading 
        threading.Thread(target=self.server.shutdown).start() 
        #self.server.shutdown()
        self.server.server_close() 
        print "# QWEBAPPEND"


######### BUILT-IN ROUTERS ###############
def __exit():
    global server
    server.stop()

def __ping():
    return "ok"

def read_diary_all():
    conn = sqlite3.connect(ROOT + '/MyDiary.db')
    c = conn.cursor()
    c.execute('SELECT * FROM diary')
    diary = c.fetchall()
    return diary

def write_diary_qpy(new_diary):
    conn = sqlite3.connect(ROOT + '/MyDiary.db')
    c = conn.cursor()
    c.execute('INSERT INTO diary VALUES (?,?)', new_diary)
    conn.commit()
    conn.close()


######### WEBAPP ROUTERS ###############
app = Bottle()
@app.route('/')
def home():
    log = read_diary_all()
    return template(ROOT+'/diaryqpy.html', diarylog=log)

@app.route('/', method = 'POST')
def write_qpy():
    headers = {'Content-Type': 'application/xml'}
    content = request.forms.get('newdiary')
    #tags = 'QPY'
    response_msg = '''
    <xml>
    <ToUserName><![CDATA[%s]]></ToUserName>
    <FromUserName><![CDATA[%s]]></FromUserName>
    <CreateTime>%s</CreateTime>
    <MsgType><![CDATA[text]]></MsgType>
    <Content><![CDATA[%s]]></Content>
    </xml>
    '''
    echostr = response_msg % ('server','phone',str(int(time.time())),content)
    r = requests.post('http://omoocpy.sinaapp.com/wechat',data=echostr, headers = headers)
    #root = ET.fromstring(r.content)
    #msg = {}
    #for child in root:
    #    msg[child.tag] = child.text

    edit_time = strftime("%Y %b %d %H:%M", localtime())
    new_diary = edit_time, content
    write_diary_qpy(new_diary)
    log = read_diary_all()
    return template(ROOT+'/diaryqpy.html', diarylog=log)


app.route('/__exit', method=['GET','HEAD'])(__exit)
app.route('/__ping', method=['GET','HEAD'])(__ping)



try:
    server = MyWSGIRefServer(host="127.0.0.1", port="8080")
    app.run(server=server,reloader=False)
except Exception,ex:
    print "Exception: %s" % repr(ex)
