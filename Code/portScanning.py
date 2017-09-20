import sys
from scapy.all import sr1,IP,ICMP, TCP, sr
from scapy.all import *
# SYN 
# p=sr(IP(dst="203.162.2.85")/TCP(sport=666,dport=[22,80,21,443], flags="S")) 

# ACK
# p=sr(IP(dst="203.162.2.85")/TCP(sport=888,dport=[21,22,80,443], flags="A")) 

# random port
# p=sr(IP(src="203.162.2.85", dst="10.1.99.2")/TCP(sport=RandShort(),
# 	dport=[20,21,80,3389]),inter=0.5,retry=2,timeout=1)
# print(p)

# TCP Connect scan
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
 
dst_ip = "203.162.2.85"
src_port = RandShort()
dst_port=80
 
# tcp_connect_scan_resp = sr1(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=10)
# if(str(type(tcp_connect_scan_resp))=="<type 'NoneType'>"):
# 	print "Closed"
# elif(tcp_connect_scan_resp.haslayer(TCP)):
# 	if(tcp_connect_scan_resp.getlayer(TCP).flags == 0x12):
# 		send_rst = sr(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="AR"),timeout=10)
# 		print "Open"
# 	elif (tcp_connect_scan_resp.getlayer(TCP).flags == 0x14):
# 		print "Closed"

# TCP flags: http://rapid.web.unc.edu/resources/tcp-flag-key/
# TCP stealth scan
stealth_scan_resp = sr1(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=10)
if(str(type(stealth_scan_resp))=="<type 'NoneType'>"):
	print "Filtered"
elif(stealth_scan_resp.haslayer(TCP)):
	if(stealth_scan_resp.getlayer(TCP).flags == 0x12):
		send_rst = sr(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="R"),timeout=10)
		print "Open"
	elif (stealth_scan_resp.getlayer(TCP).flags == 0x14):
		print "Closed"
	elif(stealth_scan_resp.haslayer(ICMP)):
		if(int(stealth_scan_resp.getlayer(ICMP).type)==3 and int(stealth_scan_resp.getlayer(ICMP).code) in [1,2,3,9,10,13]):
			print "Filtered"

# More examples of scanning techniques
# http://resources.infosecinstitute.com/port-scanning-using-scapy/#gref