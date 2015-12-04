# -*- coding: utf-8 -*- 
#qpy:webapp:MyDiaryApp
#qpy://127.0.0.1:8080/
"""
MyDiary WebApp on QPython
@Author bambooom
"""

from bottle import Bottle, ServerAdapter, run, route, request, template
import sqlite3
#import sae.kvdb
import time
from time import localtime, strftime
#import xml.etree.ElementTree as ET
import requests
import os

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#### 常量定义 #########
ROOT = os.path.dirname(os.path.abspath(__file__))
#kv = sae.kvdb.Client()

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
    c.execute('CREATE TABLE if not exists diary (time text, content text, tag text)')
    c.execute('SELECT * FROM diary')
    diary = c.fetchall()
    return diary

def write_diary_qpy(new_diary):
    conn = sqlite3.connect(ROOT + '/MyDiary.db')
    c = conn.cursor()
    c.execute('CREATE TABLE if not exists diary (time text, content text, tag text)')
    c.execute('INSERT INTO diary VALUES (?,?,?)', new_diary)
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
    message = request.forms.get('newdiary')
    tags = 'QPY'
    values = {'newdiary':message,'tags':tags}
    r = requests.post('http://omoocpy.sinaapp.com/',data=values)
    edit_time = strftime("%Y %b %d %H:%M", localtime())
    newdiary = edit_time.decode('utf-8'), message.decode('utf-8'), tags.decode('utf-8')
    write_diary_qpy(newdiary)
    log = read_diary_all()
    return template(ROOT+'/diaryqpy.html', diarylog=log)


app.route('/__exit', method=['GET','HEAD'])(__exit)
app.route('/__ping', method=['GET','HEAD'])(__ping)



try:
    server = MyWSGIRefServer(host="127.0.0.1", port="8080")
    app.run(server=server,reloader=False)
except Exception,ex:
    print "Exception: %s" % repr(ex)
