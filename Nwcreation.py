#!/usr/bin/python

from selfNetwork import Node,connection
import warnings
warnings.filterwarnings("ignore")
"""
for i in range(0,10):
	node=Node("node{}".format(i),12,IPaddr="10.10.125.11{}".format(i), MacAddr = "8c:8w:44:11:dd:0{}".format(i))

node1=Node("node1",12,["eth0","eth1","eth2","eth3"],IPaddr="10.10.125.111",MacAddr="8c:8w:44:11:dd:00")
node2=Node("node2",12,["eth0","eth1","eth2","eth3"],IPaddr="10.10.125.112",MacAddr="8c:8w:44:11:dd:01")
node3=Node("node3",12,["eth0","eth1","eth2","eth3"],IPaddr="10.10.125.113",MacAddr="8c:8w:44:11:dd:02")
node4=Node("node4",12,["eth0","eth1","eth2","eth3"],IPaddr="10.10.125.114",MacAddr="8c:8w:44:11:dd:03")
node5=Node("node5",12,["eth0","eth1","eth2","eth3"],IPaddr="10.10.125.115",MacAddr="8c:8w:44:11:dd:04")
node6=Node("node6",12,["eth0","eth1","eth2","eth3"],IPaddr="10.10.125.116",MacAddr="8c:8w:44:11:dd:05")
node7=Node("node7",12,["eth0","eth1","eth2","eth3"],IPaddr="10.10.125.117",MacAddr="8c:8w:44:11:dd:06")
node8=Node("node8",12,["eth0","eth1","eth2","eth3"],IPaddr="10.10.125.118",MacAddr="8c:8w:44:11:dd:07")
node9=Node("node9",12,["eth0","eth1","eth2","eth3"],IPaddr="10.10.125.119",MacAddr="8c:8w:44:11:dd:08")
node10=Node("node10",12,["eth0","eth1","eth2","eth3"],IPaddr="10.10.125.120",MacAddr="8c:8w:44:11:dd:09")
node11=Node("node11",12,["eth0","eth1","eth2","eth3"],IPaddr="10.10.125.121",MacAddr="8c:8w:44:11:dd:11")
node12=Node("node12",12,["eth0","eth1","eth2","eth3"],IPaddr="10.10.125.122",MacAddr="8c:8w:44:11:dd:1a")
conn1=connection("conn1")
conn2=connection("conn2")
conn3=connection("conn3")
conn4=connection("conn4")
conn5=connection("conn5")
conn6=connection("conn6")
conn7=connection("conn7")
conn8=connection("conn8")
conn9=connection("conn9")
conn10=connection("conn10")
conn11=connection("conn11")
conn12=connection("conn12")
conn1._connection__connect(node1,node2,"eth0","eth0")
conn2._connection__connect(node3,node4,"eth0","eth0")
conn3._connection__connect(node6,node5,"eth0","eth0")
conn4._connection__connect(node7,node8,"eth0","eth0")
conn5._connection__connect(node10,node9,"eth0","eth0")
conn6._connection__connect(node11,node12,"eth0","eth0")
conn7._connection__connect(node2,node3,"eth1","eth1")
conn8._connection__connect(node4,node5,"eth1","eth1")
conn9._connection__connect(node6,node7,"eth1","eth1")
conn10._connection__connect(node8,node9,"eth1","eth1")
conn11._connection__connect(node10,node11,"eth1","eth1")
conn12._connection__connect(node12,node1,"eth1","eth1")
"""
def access():
	print node1
def main():
	def sub_main():
		if "node1" not in globals():
			globals().update({"node1":50})
	sub_main()
	access()
if __name__=="__main__":
	main()
	
