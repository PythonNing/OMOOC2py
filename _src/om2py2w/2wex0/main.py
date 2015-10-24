from Tkinter import * 

master = Tk()
f = open('diary log.txt','a+')
log = StringVar()
log.set(f.read())
w = Message(master, textvariable=log) # Message Widget displays the log txt file
w.pack()

f.close()
mainloop()
