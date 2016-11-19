# Hien thi chu hello world
print("Hello World")

# Khai bao mot bien 
number_files = 100

# In gia tri cua bien
# Cach 1
print("Number of files scanned: %d " % (number_files))
# Cach 2
print("Number of files scanned: {}".format(number_files))

# Kiem tra 1 bang 1?
one_equal_one = (1 == 1)
print("1 = 1 ? {}".format(one_equal_one))

# Thay doi gia tri cua mot bien
number_files = 30

# In ket qua cua bien moi duoc cap nhat
print("Number of files scanned (updated): %d " % (number_files))

# Mot commment co nhieu dong
'''
Chuong trinh duoc dung de tinh tong 2 so
Input: 2 so nguyen
Output: Tong 2 so
'''

# Phep toan co ban
# Phep cong
print("Tong cua 1 va 1: {}".format(1 + 1))

# Phep tru
print("Hieu cua 2 va 1: {}".format(2 - 1))

# Phep nhan 
print("Tich cua 2 va 1: {}".format(2 * 1))

# phep chia
print("Thuong cua 2 va 1: {}".format(2 / 1))

# phep chia lay du
print("So du khi chia 3 cho 2: {}".format(3 % 2))

# Lay so mu
print("Lap phuong cua 3: {}".format(3 ** 3))

# Cac cau truc du lieu
# kieu chuoi ki tu
name = "mickey"

# kieu chuoi so
age = "80"

# Chu y neu khong dat cac chuoi so trong dau ngoac kep thi chuoi ban dau la mot so thuc
print(" '80' equals 80 ?: {} ".format(80 == "80"))

# Lay ki tu dau tien cua chuoi
first_char = name[0]
print("Ki tu dau tien cua bien name: {}".format(first_char))

# Cong chuoi voi chuoi
print("{}".format("mickey" + " is" + " a" + " mouse"))

# Chuyen chuoi thanh in hoa, huu dung khi ban gap du lieu o nhieu dinh dang khac nhau, nhung ngu 
# nghia khong doi
# Ban co the chuyen no ve in hoa hoac in thuong
print("mickey viet hoa: {}".format(name.upper()))

# Kieu danh sach
name_list = ['mickey', 'donald', 'tom', 'jerry']

# Lay ra ten dau tien
print("Ten cua nguoi dau tien: {}".format(name_list[0]))



# Xac dinh kich thuoc cua danh sach
print("Tong so nguoi: {}".format(len(name_list)))

# Thay mot phan tu trong danh sach dua tren index
name_list[0] = 4

# Cac phep so sanh
# So sanh bang
print("3 == 3?: {} ".format(3 == 3))

# so sanh khong bang
print("3 != 3: {}".format(3 != 3))

# So sanh lon hon
print("4 > 3?: {} ".format(4 > 3))

# so sanh lon hon hoac bang
print("4 >= 3?: {}".format(4 >= 3))

# So sanh nho hon
print("4 < 3?: {}".format(4 < 3))

# so sanh lon hon hoac bang
print("4 <= 3?: {} ".format(4 <= 3))

# su dung so sanh va re nhanh
if (4 > 3):
	print("4 lon hon 3")
else:
	print("4 nho hon 3")


# Vong lap for
for name in name_list:
	print(name)

print("Start while loop")
# Vong lap while
i = 0
while(i < len(name_list)):
	print(name_list[i])
	i = i + 1

# dinh nghia mot ham co 2 tham so va khong co gia tri tra ve
def tong(a, b):
	print (a+b)

# goi ham
tong(3, 4)

# dinh nghia mot ham co 2 tham so va tra ve tich 2 so
def tich(a, b):
	return (a * b)

# goi ham
tich_2_so = tich(3, 4)

# Hien thi ket qua tra ve
print("Tich 2 so: {}".format(tich_2_so))

# su dung mot goi thu vien
import psutil

# Liet ke cac tien trinh
print("Danh sach cac tien trinh: {}".format(psutil.pids()))