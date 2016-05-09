#!/usr/bin/python
"""
This file is used to create the UI for Network creation 
"""
import selfNetwork as sn
from Tkinter import *
from tkFileDialog import askopenfile as af
class main_window(Frame):
	def __init__(self,parent=None):
		Frame.__init__(self,parent)
		self.parent=parent
		self.frame=Frame(parent)
		self.initialize()
	def createEntry(self,cn,rw,stick):
		self.entry=Entry(self.frame)
		self.entry.grid(column=cn,row=rw,sticky=stick)
	def createButton(self,txt,rw,cn,stick,cmd=None):
		button=Button(self.frame,text=txt,command=cmd)
		button.grid(column=cn,row=rw,sticky=stick)
	def createLabel(self,cn,rw,colspan,stick,anch,txt,fore,back):
		label=Label(self.frame,anchor=anch,text=txt,fg=fore,bg=back)
		label.grid(column=cn,row=rw,columnspan=colspan,sticky=stick)
	def close(self):
		self.grid_forget()
		self.grid()
	def initialize(self):
		self.frame.grid(sticky=N+S+E+W)
		
def createNetwork():
	main_app.close()
	main_app.createLabel(0,0,4,'NEWS',"center","Network Create Node ","Black","White")
	nop=1
	for i in ["Name","ports","Interfaces","IPaddr","MacAddr","xposition","yposition","clock speed","Queue Size","Heat"]:
		main_app.createLabel(0,nop,1,'NEWS',None,i,"Black","White")
		main_app.createEntry(1,nop,'NEWS')
		nop+=1
	main_app.createButton("create",12,1,'NEWS')
def loadNetwork():
	main_app.close()
	main_app.createLabel(0,0,1,'NEWS',None,"Load Network","Black","White")
	file_name=af(mode="r")
if __name__=="__main__":
	root=Tk()
	root.title("Self Learning Network")
	main_app=main_window(parent=root)
	main_app2=main_window(parent=root)
	main_app.createButton("create Network",5,1,'NEWS',createNetwork)
	main_app.createButton("Load Network",8,1,'NEWS',loadNetwork)
	try:
		main_app.mainloop()
	except KeyboardInterrupt:
		print "Node creation process Terminated abruptly"

