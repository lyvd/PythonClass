# coding=utf-8
import subprocess, sys, nmap, os.path, grp, psutil # Chi nen su dung cac
import socket # khong su dung den
from datetime import datetime

nm = nmap.PortScanner()
# Viet tieng anh ha
print("nhập vào địa chỉ IP: ")
ip = raw_input()
ip2 = str(ip)
print("nhập vào port muốn quét(ví dụ: 22-443): ")
port = raw_input()
port2 = str(port)
print ("-" * 60)
print ("Đợi một chút, đang quét port của host {}".format(ip2))
print ("-" * 60)

# good job ;)
t1 = datetime.now()

scanport = nm.scan(ip2, port2)
a=scanport['scan'][ip2]
print("Trạng thái của host {}: {}".format(ip2, a['status']['state']))

for i in a['tcp']:
    b=a['tcp'][i]
    print("Port {}: {}\n   Product: {}\n   Version: {}\n   Name: {}".format(i,b['state'],b['product'],b['version'],b['name']))

t2 = datetime.now()
t = t2 - t1
print ("Thời gian quét: {}".format(t))