#!/bin/bash

iptables -A INPUT -p tcp --sport 6666 --dport 80 -j NFQUEUE --queue-num 0
