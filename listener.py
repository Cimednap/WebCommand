#!/usr/bin/python 

from netfilterqueue import NetfilterQueue
from scapy.all import *

#############################################################################################
##Function: CheckPacket
##Purpose: Checks the packet for certain Base64 encoded strings, executes commands if found
##Returns: none
#############################################################################################
def CheckPacket(packet1):

    ret = "\n".join(packet1.sprintf("{Raw:%Raw.load%}\n").split(r"\r\n"))
    #ret += "nothing to be seen here"
    if "bmV0Y2F0" in ret:
     	print "Executing Netcat on port 7777\n"
     	#execute your commands here

    elif "ZHJvcGZ3" in ret:
    	print "Executing IPtables -F\n"
    	#execute your commands here
    else:
    	print "string not found"


#############################################################################################
##Function: HandlePacket
##Purpose: Passes the data from the packet pulled from the QUEUE to the CheckPacket function,
##		   also drops the packet 
##Returns: none
#############################################################################################
def HandlePacket(pkt):
	data = pkt.get_payload()
	newPacket = IP(data)
	test = CheckPacket(newPacket)
	pkt.accept()

#Main Function 

#Initialize Netfilter object
nfqueue = NetfilterQueue()

#Bind object to queue number (must match IPtables rule) / set callback function to pass packet to
nfqueue.bind(0, HandlePacket)

#Run the program until Keyboard Interrupt
try:
	nfqueue.run()
except KeyboardInterrupt:
	print('')

