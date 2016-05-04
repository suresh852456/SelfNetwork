#!/usr/bin/python
"""
This document is used to create xml writing for saving the Network configuration
"""
from xml.etree.ElementTree import Element,SubElement,Comment,tostring
Network= Element('Network')
node=SubElement(Network,"Node")
node_name=SubElement(node,"name")
node_name.text="node1"
node_ports=SubElement(node,"ports")
node_ports.text="12"
node_interfaces=SubElement(node,"interfaces")
node_interfaces.text="eth0,eth1,eth2,eth3"
node_Ipaddr = SubElement(node,"IPaddr")
node_Ipaddr.text="192.168.2.1"
print tostring(Network)


 
