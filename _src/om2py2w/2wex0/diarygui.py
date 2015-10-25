# -*- coding: utf-8 -*- 
# ------------2w task:simple diary GUI-----------
# --------------created by bambooom--------------      

from Tkinter import *  # import Tkinter module
from ScrolledText import * # ScrolledText module = Text Widget + scrollbar

import sys
reload(sys)
sys.setdefaultencoding('utf8') # change the default encoding to utf-8

class Application(Frame):
	
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

	def getnew(self,event): 
	# When press ENTER, write diary to local file
	# and print out it in Text frame
	# and also clear the Entry box
		line = self.newlog.get()
		f = open('diary log.txt','a+')
		f.write('%s\n' % line)
		f.close()
		self.t.insert(END,"%s\n" %line)
		self.t.see(END)
		self.e.delete(0,END)

	def createWidgets(self):   
		self.newlog = StringVar(self) # define StringVar
		
		self.l = Label(self, text = "Input here: ") # Label Widget 提示输入
		self.l.grid(row = 0, column = 0, sticky = W)
		
		self.e = Entry(self, textvariable = self.newlog, width = 80) # Entry box 输入框
		self.e.bind("<Return>", self.getnew) # bind ENTER to function getnew
		self.e.grid(row = 0, column = 1, sticky = W)
		self.e.focus_set() # make the mouse focus on the entry box
		
		self.t = ScrolledText(self) # ScrolledText 打印出文档的框
		self.t.grid(columnspan = 2, sticky = W)
		f = open('diary log.txt','a+') 
		self.t.insert(END,f.read()) 
		self.t.see(END)
		
		self.b = Button(self, text="QUIT", fg="red", command=self.quit) # 退出的button
		self.b.grid(row = 2, column = 0, sticky = W)

def main():
	root = Tk()
	root.title('MyDiary Application')
	root.geometry("660x450+400+100")
	app = Application(root)
	app.mainloop()

if __name__ == "__main__":
    main()
