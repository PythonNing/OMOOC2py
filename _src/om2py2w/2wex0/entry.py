from Tkinter import *
from time import localtime, strftime

master = Tk()
newlog = StringVar()
e = Entry(master, textvariable=newlog)

def getnew(event):
	line = newlog.get() # get input 
	f = open('diary log.txt','a+')
	edit_time = strftime("%a, %Y %b %d %H:%M:%S", localtime())
	f.write('%s     %s\n' % (edit_time, line))
	f.close()
	e.delete(0,END) # delete input
	
e.bind("<Return>",getnew) # bind the keyboard ENTER as function getnew
e.pack()

mainloop()
