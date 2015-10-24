# -*- coding: utf-8 -*-         

from Tkinter import *

def getnew(event):
	line = newlog.get()
	f = open('diary log.txt','a+')
	f.write('%s\n' % line)
	f.close()
	t.insert(END,"\n%s" %line)
	e.delete(0,END)

#def makeWin():
#	global newlog
win=Tk()
win.geometry("300x450+500+100")
win.title("MyDiary Application")
newlog=StringVar()
	
frame1=Frame(win)
frame1.pack()
	
e=Entry(frame1,textvariable=newlog,width=80)
e.pack(anchor=W,expand=YES)
#e.bind("<Return>",getnew)
	#e.delete(0,END)
	
frame2=Frame(win)
frame2.pack()
s=Scrollbar(frame2)
t=Text(frame2)
s.pack(side=RIGHT,fill=Y)
t.pack(side=LEFT,fill=Y)
s.config(command=t.yview)
t.config(yscrollcommand=s.set)
f = open('diary log.txt','a+')		
log=f.read()
t.insert(END,log)
	#t.insert(END,newlog)
e.bind("<Return>",getnew)

#frame3=Frame(win)	
b = Button(win, text="QUIT", fg="red", command=win.quit)
b.pack(anchor=W,side = BOTTOM)	

	#return win

#win = makeWin()
#win.mainloop()
mainloop()
