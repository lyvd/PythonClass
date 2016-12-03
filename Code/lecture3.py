# khai bao mot kieu tu dien
dict_process = {"pid": 321, "name" : "http"} 

# Lay ra gia tri cua key pid cua bien tu dien
print("PID: {}".format(dict_process["pid"]))

# Thay doi gia tri cua pid
dict_process["pid"] = 321

# In ra tu dien
print("PID sau: {}".format(dict_process["pid"]))

# Them key
dict_process["start_time"] = 12


# In ra tu dien
print("starting time: {}".format(dict_process["start_time"]))

# Xoa mot key
del dict_process["name"]

# In ra danh sach cac key
print("Danh sach cac keys: {}".format(dict_process.keys()))

# In ra tu dien: key-value
for key in dict_process.keys():
	print("{}: {}".format(key, dict_process[key]))

# Install nmap: sudo apt-get install nmap
# install python-nmap: sudo pip install python-nmap

# import nmap de su dung 
import nmap

# Initialize nmap scanner
nm = nmap.PortScanner()

# scan localhost, port 22-443
scan_result = nm.scan('127.0.0.1', '22-443')

# xac dinh kieu tra ve
print("Result type: {}".format(type(scan_result)))

# In ra gia tri
print("Scan result: {}".format(scan_result))
# Neu la kieu tu dien
# In ra danh sach cac key
print("Danh sach key: {}".format(scan_result.keys()))

# co 2 key, nmap va scan
# Tiep tuc xem 2 key chua kieu du lieu
for key in scan_result.keys():
	print("key {}: type {}".format(key, format(type(scan_result[key]))))

# Lay ra thong tin scan
print("Scan info: {}".format(scan_result["nmap"]["scaninfo"]))
print("Scan info: {}".format(nm.scaninfo()))

# Lay ra trang thai port
print("Trang thai cua port 80: {}".format(nm['127.0.0.1']['tcp'][80]['state'])) 

# lay ra tat ca cac ports cua thuoc giao thuc tcp
print("Tat cac cac ports cua tcp: {}".format(nm['127.0.0.1'].all_tcp()))

# In ra ket qua nhu csv
print("CSV style: {}".format(nm.csv()))

# install pymongo: sudo pip install pymongo
# import pymongo
from pymongo import MongoClient

# ket noi toi co so du lieu
client = MongoClient('mongodb://localhost:27017/')

# create database
mydb = client['dataset']

# record
record = {"hash" : file_hash, "doc":document, "length": doc_len, "av_label": av_label, "chars": dist_char}

# insert
record_id = mydb.dataset.insert(record) 