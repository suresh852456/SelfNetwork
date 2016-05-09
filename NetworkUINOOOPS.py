#!/usr/bin/python
"""
This file is used to create the UI for Network creation 
"""
import selfNetwork as sn
from Tkinter import *
from tkFileDialog import askopenfile as af
import socket	
class main_application(Frame):
	def __init__(self,parent):
		Frame.__init__(self,parent)
		self.parent=parent
		self.grid()
def refresh(widget):
	widget.grid_forget()
	widget.destroy()
def createButton(parent,txt,rw,cn,stick,cmd=None):
	return Button(parent,text=txt,command=cmd).grid(column=cn,row=rw,sticky=stick)
def createLabel(parent,cn,rw,colspan,stick,anch,txt,fore,back):
	Label(parent,anchor=anch,text=txt,fg=fore,bg=back).grid(column=cn,row=rw,columnspan=colspan,sticky=stick)
def exit():
	root.quit()
def saveNetwork():
	pass
def cancel():
	global main_app
	refresh(main_app)
	main_app=main_application(root)
	createButton(main_app,"create Network",5,1,'NEWS',createNetwork)
	createButton(main_app,"Load Network",8,1,'NEWS',loadNetwork)
	createButton(main_app,"save network",9,1,'NEWS',saveNetwork)
	createButton(main_app,"Exit",10,1,'NEWS',exit)	
def createNode(Error=False):
	global main_app
	refresh(main_app)
	main_app=main_application(root)
	if Error:
		createLabel(main_app,0,0,4,'NEWS',"center","Type error Try! again ","Red","White")
		
	else:
		createLabel(main_app,0,0,4,'NEWS',"center","Network Create Node ","Black","White")	
	nop=1
	
	for i in ["Name","Ports","Interfaces","IPaddr","MacAddr","Xposition","Yposition","Clockspeed","QueueSize","Heat"]:
		createLabel(main_app,0,nop,1,'NEWS',None,i,"Black","White")
		nop+=1		
	name=Entry(main_app)
	name.grid(column=1,row=1,sticky='NEWS')
	ports=Entry(main_app)
	ports.grid(column=1,row=2,sticky='NEWS')
	interfaces=Entry(main_app)
	interfaces.grid(column=1,row=3,sticky='NEWS')
	ipaddr=Entry(main_app)
	ipaddr.grid(column=1,row=4,sticky='NEWS')
	macaddr=Entry(main_app)
	macaddr.grid(column=1,row=5,sticky='NEWS')
	xposition=Entry(main_app)
	xposition.grid(column=1,row=6,sticky='NEWS')
	yposition=Entry(main_app)
	yposition.grid(column=1,row=7,sticky='NEWS')
	clockspeed=Entry(main_app)
	clockspeed.grid(column=1,row=8,sticky='NEWS')
	queuesize=Entry(main_app)
	queuesize.grid(column=1,row=9,sticky='NEWS')
	heat=Entry(main_app)
	heat.grid(column=1,row=10,sticky='NEWS')
	def on_create():
		try:
			try:
				socket.inet_aton(ipaddr.get())
				if str(name.get()) not in globals():
					globals().update({str(name.get()):sn.Node(str(name.get()),int(ports.get()),str(interfaces.get()).split(","),str(ipaddr.get()),str(macaddr.get()),int(xposition.get()),int(yposition.get()),float(clockspeed.get()),int(queuesize.get()),int(heat.get()))})
					createLabel(main_app,0,0,4,'NEWS',"center","Node Creation Success ","Black","White")
				else:
					createLabel(main_app,0,0,4,'NEWS',"center","Node Creation failure ","Black","White")
			except socket.error:
				createNode(True)
			global main_app
			refresh(main_app)
			main_app=main_application(root)
			createButton(main_app,"create anoter Node",5,1,'NEWS',createNode)
			createButton(main_app,"create Connection",6,1,'NEWS',createConnection)
			createButton(main_app,"Build Network",7,1,'NEWS',buildNetwork)
			createButton(main_app,"save network",8,1,'NEWS',saveNetwork)
			createButton(main_app,"cancel",9,1,'NEWS',cmd=cancel)
		except ValueError:
			createNode(True)
	createButton(main_app,"create",12,1,'NEWS',cmd=on_create)
	createButton(main_app,"cancel",12,0,'NEWS',cmd=cancel)
def createConnection(Error=False):	
	global main_app
	refresh(main_app)
	main_app=main_application(root)
	if Error:
		createLabel(main_app,0,0,4,'NEWS',None,"Error Try again","Red","White")
	else:
		createLabel(main_app,0,0,4,'NEWS',None,"Network create Connection","Black","White")
	nop=1
	for i in ["Name","length","type of connection","medium","Node 1","Node 2","Node 1 interface","Node 2 interface"]:
		createLabel(main_app,0,nop,1,'NEWS',None,i,"Black","White")
		nop+=1
	name=Entry(main_app)
	name.grid(column=1,row=1,sticky='NEWS')
	length=Entry(main_app)
	length.grid(column=1,row=2,sticky='NEWS')
	typeof=Entry(main_app)
	typeof.grid(column=1,row=3,sticky='NEWS')
	medium=Entry(main_app)
	medium.grid(column=1,row=4,sticky='NEWS')
	node1=Entry(main_app)
	node1.grid(column=1,row=5,sticky='NEWS')
	node2=Entry(main_app)
	node2.grid(column=1,row=6,sticky='NEWS')
	node1if=Entry(main_app)
	node1if.grid(column=1,row=7,sticky='NEWS')
	node2if=Entry(main_app)
	node2if.grid(column=1,row=8,sticky='NEWS')
	def on_create():
		try:
			if str(name.get()) not in globals():
				globals().update({str(name.get()):sn.connection(str(name.get()),int(length.get()),str(typeof.get()),str(medium.get()),str(node1.get()),str(node2.get()),str(node1if.get()),str(node2if.get()))})
				for key in globals().keys():
					if key==node1.get():
						key.connect(str(node1if.get()),str(node2.get()))
				for key in globals().keys():
					if key==node2.get():
						key.connect(str(node2if.get()),str(node1.get()))
				global main_app
				refresh(main_app)
				main_app=main_application(root)
				createLabel(main_app,0,0,4,'NEWS',"center","Connection Creation Success ","Black","White")
			else:
				createLabel(main_app,0,0,4,'NEWS',"center","Connection Creation Failures ","Black","White")
			createButton(main_app,"create Node",5,1,'NEWS',createNode)
			createButton(main_app,"create another Connection",6,1,'NEWS',createConnection)
			createButton(main_app,"Build Network",7,1,'NEWS',buildNetwork)
			createButton(main_app,"save network",8,1,'NEWS',saveNetwork)
			createButton(main_app,"cancel",9,1,'NEWS',cmd=cancel)
		except ValueError:
			createConnection(True)
	createButton(main_app,"create",12,1,'NEWS',cmd=on_create)
	createButton(main_app,"cancel",12,0,'NEWS',cmd=cancel)
def createNetwork():
	global main_app
	refresh(main_app)
	main_app=main_application(root)
	createLabel(main_app,0,0,2,'NEWS',None,"Node or Connection","Black","White")
	createButton(main_app,"create Node",1,1,'NEWS',createNode)
	createButton(main_app,"create Connection",2,1,'NEWS',createConnection)
	createButton(main_app,"cancel",3,1,'NEWS',cmd=cancel)
def loadNetwork():
	global main_app
	refresh(main_app)
	main_app=main_application(root)
	createLabel(main_app,0,0,1,'NEWS',None,"Load Network","Black","White")
	createButton(main_app,"cancel",3,0,'NEWS',cmd=cancel)
	file_name=af(mode="r")
def main():
	global root
	global main_app
	root=Tk()
	root.title("Self Learning Network")
	main_app=main_application(root)
	createButton(main_app,"create Network",5,1,'NEWS',createNetwork)
	createButton(main_app,"Load Network",8,1,'NEWS',loadNetwork)
	createButton(main_app,"Exit",10,1,'NEWS',exit)
	try:
		main_app.mainloop()
	except KeyboardInterrupt:
		print "Program Terminated abruptly"
if __name__=="__main__":
	main()
