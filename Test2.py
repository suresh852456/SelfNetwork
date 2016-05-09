from xml.etree import ElementTree as ET
tree= ET.parse('netconf.xml')
#root=tree.getroot()
from tkFileDialog import askopenfile as af
def go_further(tree):
	root=tree.getroot()
	for children in root.findall('Node'):
		for i in ('name','ports','interfaces','IPaddr','macaddr','xpos','ypos','clockspeed','queuesize','Heat'):
			yield children.find(i).text
	for children in root.findall('connection'):
		for i in ('name','node1','node2','node1if','node2if','length','typeofconn','medium'):
			yield children.find(i).text
	

re=go_further(tree)
print re
"""
a=af(mode="r")
print type(a)
tr=ET.parse(a)
trrt=tr.getroot()
print trrt.tag
"""
