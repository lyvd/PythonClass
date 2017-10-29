print("Hello world")

# De comment code trong python ta dung dau #

number_files = 100
# cac ban co the in gia tri cua bien dung 2 cach
# Cach 1 giong nhu C
# de di chuyen con chuot ve dau dong ta nhan nut esc va o
# de di chuyen con chuot toi dong tiep theo nhan nut esc va +
# dung %d de in integer, %s de in string 
print("Gia tri cua bien number_files : %d" % number_files)

# khai bao mot bien kieu string
ten_hv = "Bac"
# Muon in ten hoc vien Bac
# chu y hoc vien la kieu string, kieu nay duoc nhan dang boi hai dau nngoac kep

print("Hoc vien : %s" %ten_hv)

# now in ra ten hoc vien va tuoi hoc vien
# can khai bao ra mot bien tuoi
tuoi_hv = 21

# Minh phai dung %s va %d de tro toi cac bien phia sau. 
print("Hoc vien: %s, Tuoi: %d" %(ten_hv, tuoi_hv))

# gio anh bo thu %s va %d xem sao nhe ;)
#print("Hoc vien: , Tuoi: " (ten_hv, tuoi_hv))

# mot cach khac trong python, de hon xu dung ham format
# {0} nghia la bien dau tien muon in, ten_hv la {0} 
# khoi can phai nho la kieu integer hay string cho met

print("Ten hoc vien: {0}".format(ten_hv))
# gio anh muon in ten hoc vien va tuoi hoc vien luon

# {0} la bien thu nhat, {1} la bien thu 2. Tuong tu voi 3 hay 4
print("Hoc vien: {0}, Tuoi: {1}".format(ten_hv, tuoi_hv))

# marriged or not
marriage = "no"

# Dien vao cho trong ? :D
print("Tuoi: {1}, Ten: {0}".format(ten_hv, tuoi_hv))
# {0}: ten_hv, {1}: tuoi_hv, {2}: marrigage. Theo thu tu. Hoac muon doi lai cung khong sao
# cong tru nhan chia trong python cung don gian :d
a = 1 
b = 2
# tiep tuc dien vao cho trong voi cac phep nnhan chia :v

print("cong: {0}, nhan: {1}".format(a+b, a *b))

# so sanh mot string va mot integer
so = 10
chuoi = "10"

# lieu so va chuoi co giong nhau ?
# su dung if, else trong python

# cac em chu y, trong python khi viet mot cau lenh dieu kien ta phai thut dau dong, vi du
# thuong la mot tab = 4 spaces
# co the lam nhu sau
# go :setexpandtab shiftwidth=4 tabstop=4
if so == chuoi:
    print("YES EQUAL")
else:
    print("no")
