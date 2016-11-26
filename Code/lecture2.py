import os.path
# get file name 
path = "/home/lyvd/Documents/test.txt"

# phan tach cac thanh phan trong duong dan
file_path = os.path.split(path)

# file name
file_name = file_path[-1]
print("File name: {}".format(file_name))

# Hoac ngan gon hon co the su dung ham basename() 
file_name1 = os.path.basename(path)
print("File name: {}".format(file_name1))

# Lay ten thu muc chua file
# Cach 1, dung ket qua tra ve tu ham split
file_dir = file_path[0]
print("File name: {}".format(file_dir))
# Cach 2 dung ham dirname()
file_dir1 = os.path.dirname(path)
print("File name: {}".format(file_dir1))

# Neu muon lay  phan mo rong (extension) vi du, txt, pdf...
file_ext = os.path.splitext(path)
print("File with an extension: {}".format(file_ext[-1]))

# Tao mot duong dan huu ich khi tao mot thu muc hay tep tin moi
my_path = ['/','home', 'lyvd', 'Documents', 'secret.txt']
# Ki tu * duoc dung de unpack cac gia tri trong mot sequence ra thanh cac phan tu (theo vi tri)
new_path = os.path.join(*my_path)
print("New path: {}".format(new_path))

# Liet ke cac users tren he thong
import grp
groups = grp.getgrall()
for groupId, group in enumerate(groups):
	print("Group {}: {}".format(groupId, group))
	# list users in groups
	for userId, user in enumerate(group):
		print("User {}: {}".format(userId, user))

# tao moi thu muc rieng cho tung user
user_list = ['lyvd', 'mickey']
# lap qua danh sach cac user
for user in user_list:
	# tim kiem user
	lookup = '~' + user
	print("Mo rong duong dan user cua user {}: {}".format(lookup, os.path.expanduser(lookup)))

# chuan hoa cac duong dan sai
wrong_path = "/home/lyvd//Documents/test.txt"
normal_path = os.path.normpath(wrong_path)
print("Duong dan sau khi chuan hoa: {}".format(normal_path))

# Chuyen tu duong dan tuong doi sang duong dan tuyet doi
relative_path = "./Desktop/"
absolute_path = os.path.abspath(relative_path)
print("Duong dan tuyet doi: {}".format(absolute_path))

# Kiem tra duong dan chi toi mot thu muc hay mot tep tin
# Truong hop thu muc
path = "/home/lyvd/Documents"
print("Duong dan co ton tai ? : {}".format(os.path.exists(path)))
print("Duong dan chi toi mot thu muc ?: {}".format(os.path.isdir(path)))
print("Duong dan chi toi mot tep tin ?: {}".format(os.path.isfile(path)))

#path = "/etc"
# Liet ke tat ca cac files trong mot thu muc
import os

# Liet ke cac users tren he thong
import grp

groups = grp.getgrall()

print(type(groups))

for group in groups:
	if group.gr_name == "it":

		print("Group: {}".format(group))
		print("Group members: {}".format(group.gr_mem))
		print("Ten group: {}".format(group.gr_name))


f = []
for (dirpath, dirnames, filenames) in os.walk(path):
    f.extend(filenames)
    print type(filenames)
    print(dirpath)
    break
print(type(dirnames))

new_dir = os.path.join(path, "New Document")
# Neu thu muc moi khong ton tai
if not os.path.exists(new_dir):
	# tao thu muc moi
	os.makedirs(new_dir)

# Lay thong tin ve cpu
import psutil
print(psutil.cpu_times())
for i in (psutil.cpu_times()):
	print(i)

# Liet ke cac tien trinh
print(psutil.pids())

# Su dung dia cung
print(psutil.disk_usage('/home/lyvd/Documents'))

# IP
ipInfo = (psutil.net_if_addrs())
for key, value in ipInfo.items():
	print("Key {}: {}".format(key, value))