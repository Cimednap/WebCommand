#!/usr/bin/python 

from netfilterqueue import NetfilterQueue
from scapy.all import *

pkt=Ether(src=”00:13:37:00:17:bb”)/IP(src=”192.168.111.17”,dst=”192.168.111.132”)/TCP(dport=80,sport=6666)/”GET /index.html bmV0Y2F0\n”

sendp(pkt) 
