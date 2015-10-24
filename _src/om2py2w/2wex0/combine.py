# -*- coding: utf-8 -*-         

# -*- coding: utf-8 -*-         

from Tkinter import *

master = Tk()
master.geometry("300x450+500+100")
master.title("MyDiary Application")
log = StringVar()
newlog = StringVar()

frame = Frame(master)
frame.pack()
e = Entry(frame, textvariable=newlog,bg="green")

def getnew(event):
	line = newlog.get() # get input 
	#f = open('diary log.txt','a+')
	#f.write('%s\n' % line)
	#f.close()
	#ml=Label(frame, text = line)
	#ml.pack(anchor=W,fill=X,after=m)
	
	m = Message(frame, text=line)
	m.pack(anchor=W)
	
	e.delete(0,END)

e.bind("<Return>",getnew) # bind the keyboard ENTER as function getnew
e.pack(anchor=W,fill=X)

f = open('diary log.txt','a+')		
log.set(f.read())
m = Message(frame, textvariable=log)
m.pack(anchor=W)
	
b = Button(master, text="QUIT", fg="red", command=frame.quit)
b.pack(anchor=W,side = BOTTOM)

mainloop()
