#!/usr/bin/python
"""
This file is used to create the UI for Network creation 
"""
import selfNetwork as sn
from Tkinter import *
from tkFileDialog import askopenfile as af
import socket
from types import InstanceType
from xml.etree.ElementTree import Element,SubElement,Comment,tostring
from xml.dom import minidom

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
	parent=Element("Network")
	parent.set('version','1.0')
	parent.set('encoding','UTF-8')
	parent.append(Comment("Self Learning Network Configuration"))
	for i in list(globals().iteritems()):
		if type(i[1]) is InstanceType:
			if str(i[1]).startswith("<selfNetwork.Node"):
				node=SubElement(parent,"Node")
				SubElement(node,"name").text=globals()[i[0]].name
				SubElement(node,"ports").text=str(globals()[i[0]].ports)
				SubElement(node,"interfaces").text=",".join(globals()[i[0]].interfaces)
				SubElement(node,"IPaddr").text=globals()[i[0]].IPaddr
				SubElement(node,"macaddr").text=globals()[i[0]].MacAddr
				SubElement(node,"xpos").text=str(globals()[i[0]].xpos)
				SubElement(node,"ypos").text=str(globals()[i[0]].ypos)
				SubElement(node,"clockspeed").text=str(globals()[i[0]].clockSpeed)
				SubElement(node,"queuesize").text=str(globals()[i[0]].QueueSize)
				SubElement(node,"Heat").text=str(globals()[i[0]].heat)
			if str(i[1]).startswith("<selfNetwork.connection"):
				conn=SubElement(parent,"Connection")
				SubElement(conn,"name").text=globals()[i[0]].name
				SubElement(conn,"node1").text=globals()[i[0]].node1
				SubElement(conn,"node2").text=globals()[i[0]].node2
				SubElement(conn,"ndoe1if").text=globals()[i[0]].node1if
				SubElement(conn,"node2if").text=globals()[i[0]].node2if
				SubElement(conn,"length").text=str(globals()[i[0]].length)
				SubElement(conn,"typeofconn").text=globals()[i[0]].typeofconn
				SubElement(conn,"medium").text=globals()[i[0]].medium
	xml_file=open("netconf.xml","wb")
	xml_file.writelines(minidom.parseString(tostring(parent, 'utf-8')).toprettyxml(indent="  "))
	xml_file.close()

				
def cancel():
	global main_app
	refresh(main_app)
	main_app=main_application(root)
	createButton(main_app,"create Network",5,1,'NEWS',createNetwork)
	createButton(main_app,"Load Network",8,1,'NEWS',loadNetwork)
	createButton(main_app,"save network",9,1,'NEWS',saveNetwork)
	createButton(main_app,"Exit",10,1,'NEWS',exit)
def buildNetwork():
	for i in list(globals().iteritems()):
		if type(i[1]) is InstanceType:
			if str(i[1]).startswith("<selfNetwork.connection"):
				if i[1].node1 in globals():
					globals()[i[1].node1].connect(i[1].node1if,i[1].node2)
				if i[1].node2 in globals():
					globals()[i[1].node2].connect(i[1].node2if,i[1].node1)
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
		if i.lower() in globals():
			del globals()[i.lower()]
		if i.lower() not in globals():
			globals().update({i.lower():Entry(main_app)})
			globals()[i.lower()].grid(column=1,row=nop,sticky='NEWS')
		nop+=1	
	def on_create(name,ports,interfaces,ipaddr,macaddr,xposition,yposition,clockspeed,queuesize,heat):
		try:
			if (len(str(ipaddr).split("."))!=4):	
				raise socket.error
			socket.inet_aton(ipaddr)
			if name in globals():
				del globals()[name]
			if name not in globals():
				globals().update({name:sn.Node(name,int(ports),interfaces.split(","),ipaddr,macaddr,int(xposition),int(yposition),float(clockspeed),int(queuesize),int(heat))})
				success=True
			else:
				success=False		
			global main_app
			refresh(main_app)
			main_app=main_application(root)
			if success:
				createLabel(main_app,0,0,4,'NEWS',"center","Node Creation Success ","Black","White")
			else:
				createLabel(main_app,0,0,4,'NEWS',"center","Node Creation Failure ","Black","White")
			createButton(main_app,"create anoter Node",5,1,'NEWS',createNode)
			createButton(main_app,"create Connection",6,1,'NEWS',createConnection)
			createButton(main_app,"Build Network",7,1,'NEWS',buildNetwork)			
			createButton(main_app,"save network",8,1,'NEWS',saveNetwork)
			createButton(main_app,"cancel",9,1,'NEWS',cmd=cancel)
		except (ValueError , socket.error) as e:
			createNode(True)
	createButton(main_app,"create",12,1,'NEWS',cmd= lambda : on_create(name.get(),ports.get(),interfaces.get(),ipaddr.get(),macaddr.get(),xposition.get(),yposition.get(),clockspeed.get(),queuesize.get(),heat.get()))
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
	for i in ["Name","Length","Typeofconnection","Medium","Node1","Node2","Node_1_interface","Node_2_interface"]:
		createLabel(main_app,0,nop,1,'NEWS',None,i,"Black","White")
		if i.lower() in globals():
			del globals()[i.lower()]
		if i.lower() not in globals():
			globals().update({i.lower():Entry(main_app)})
			globals()[i.lower()].grid(column=1,row=nop,sticky='NEWS')	
		nop+=1
	def on_create(name,node1,node2,node1if,node2if,length,typeofconnection,medium):
		try:
			if name in globals():
			  	del globals()[name]
			if name not in globals():
				globals().update({name:sn.connection(name,node1,node2,node1if,node2if,float(length),typeofconnection,medium)})
				success=True
			else:
				success=False			
			global main_app
			refresh(main_app)
			main_app=main_application(root)
			if success:
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
	createButton(main_app,"create",12,1,'NEWS',cmd= lambda : on_create(name.get(),node1.get(),node2.get(),node_1_interface.get(),node_2_interface.get(),length.get(),typeofconnection.get(),medium.get()))
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
