# -*- coding: utf-8 -*-
# 1w task
# dairy system

import os
from time import localtime, strftime

def dairy():
	print """
	Choose from the menu below:
	1. Write new dairy
	2. Read previous dairy
	3. Quit """
	
	choice = raw_input('Input 1/2/3 >') # ask for choosing from menu
	
	if choice == '1':
		write() # write new dairy
	elif choice == '2':
		read() # read previous dairy
	elif choice == '3':
		os._exit(0) # exit the script
	else:
		print 'Wrong number. Choose again!'
		dairy() # return to the beginning menu

def write():
	f = open('new dairy.txt','a') 
	line = raw_input('Input here >')
	edit_time = strftime("%a, %Y %b %d %H:%M:%S", localtime())
	f.write('%s     %s\n' % (edit_time, line))
	f.close()
	dairy()

def read():
	f = open('new dairy.txt','a+')
	print 'Below is the previous dairy.'
	print f.read()
	dairy()
	
dairy()
