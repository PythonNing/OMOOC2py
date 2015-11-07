# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
MyDiary Web Application
'''

from bottle import request, route, run, template

def check_login(username, password):
	if username == 'abc' and password == 'abc':
		return True
	else:
		return False


@route('/mydiary')
def start():
	return template('diaryweb', diarylog='hello world')

@route('/mydiary', method='POST')
def input_new():
	newdiary = request.forms.get('newdiary')
	return template('diaryweb', diarylog='hello world \n'+newdiary)

#@route('/login', method='POST')
#def do_login():
#	username = request.forms.get('username')
#	password = request.forms.get('password')
#	if check_login(username, password):
#		return "<p>Your login information was correct.</p>"
#	else:
#		return "<p>Login failed.</p>"

if __name__ == '__main__':
	run(host='localhost', port=8250, debug=True, reloader=True)
	
