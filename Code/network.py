import sys
from scapy.all import sr1,IP,ICMP, TCP, sr

# Ping from a real IP
# p=sr1(IP(dst="8.8.8.8", ttl =118)/ICMP()/"Hello World")

# Ping from a fake IP
#p=sr1(IP(src="10.0.99.100",dst="8.8.8.8")/ICMP()/"Hello World")


#Which one got a reply?

# Add ttl
#p=sr1(IP(dst="8.8.8.8", ttl =118)/ICMP()/"Hello World")

# ping reply
# p=sr1(IP(dst="8.8.8.8")/ICMP(type = 0)/"Hello World")

# SYN packet
# ip=IP(src='172.16.120.5',dst='8.8.8.8')
# SYN=TCP(sport=1024,dport=443,flags='S',seq=1000)
# SYNACK=sr1(ip/SYN)

# if SYNACK:
#     SYNACK.show()

# make a tcp connection to an ip port 80
p=sr(IP(dst="192.30.253.113")/TCP(dport=443)) 

# parse the result
# ans,unans  = _

# print ans
# # if p:
# #     p.show()



# default port of scapy

#multi destination ports
# p=sr(IP(dst="116.193.76.7")/TCP(dport=[23,80,53])) 

if p:
    print p

