# -*- coding: utf-8 -*- 
# ----------1w task:simple diary system----------
# --------------created by bambooom--------------         

from time import localtime, strftime

def diary():
	f = open('diary log.txt','a+')
	print 'Below is the previous dairy.'
	print f.read() # print out the previous diary log
	
	f = open('diary log.txt','a') # re-open the file to write
	line = raw_input('Input New Diary >')
	a = ['q','quit']
	b = ['h','help','?']
	
	while line.lower() not in a: # while not to quit, loop to ask for input 	 	
		if line.lower() in a: 
			break # to quit the loop, not to input new diary
		elif line.lower() in b:
			print """ 
			Input h/help/? for help.
			Input q/quit to quit the process.
			""" # print the help
		
		edit_time = strftime("%a, %Y %b %d %H:%M:%S", localtime())
		f.write('%s     %s\n' % (edit_time, line))
		line = raw_input('Input New Diary >')
	
	print 'Bye! Good Day!'
	f.close()

if __name__ == '__main__':
	diary()
