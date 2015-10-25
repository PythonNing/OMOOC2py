# -*- coding: utf-8 -*- 
# ------------2w task:simple diary GUI-----------
# --------------created by bambooom--------------      


from Tkinter import *  # import Tkinter module
from ScrolledText import * # ScrolledText module = Text Widget + scrollbar

global newlog

class Application(Frame):  # 基本框架

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):   # 组件
        newlog = StringVar()

        l = Label(self, text = "Input here: ") # Label Widget 提示输入
        l.grid(row = 0, column = 0, sticky = W)

        e = Entry(self,textvariable=newlog,width=80) # Entry box 输入框
        e.grid(row = 0, column = 1, sticky = W)

        t = ScrolledText(self) # ScrolledText 打印出文档的框
        t.grid(columnspan = 2, sticky = W)

        b = Button(self, text="QUIT", fg="red", command=self.quit) # 退出的button
        b.grid(row = 2, column = 0, sticky = W)


root = Tk()
root.title('MyDiary Application')
app = Application(root)

# 主消息循环:
app.mainloop()
