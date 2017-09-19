# # import os.path
# # # get file name 
# # path = "/home/lyvd/Documents/test.txt"

# # # phan tach cac thanh phan trong duong dan
# # file_path = os.path.split(path)

# # print(type(file_path))

# # for i in file_path:
# # 	print i

# # file_name1 = os.path.basename(path)
# # print("File name: {}".format(file_name1))
# import os
# # path = "/home/lyvd/python class/bin"

# # for (dirpath, dirnames, filenames) in os.walk(path):
# # 	print(filenames)

# # path = "/home/lyvd/python_class/storehere/"
# # # print("cd " + path)
# # os.chdir(path)
# # # os.system("cd " + path)
# # (os.system("touch python.txt"))

# # my_path = ['/','home', 'lyvd', 'Documents', 'secret.txt']

# # new_path = os.path.join(*my_path)

# # print(new_path)

# # wrong_path = "///home//lyvd"
# # print(os.path.normpath(wrong_path))

# path = "/home/lyvd/python_class/storehere/python.txt"
# # import os.path
# # import time
# # print(os.path.getsize(path))
# # print(time.ctime(os.path.getmtime(path)))
# # print(os.path.isdir(path))

# import hashlib
# print hashlib.sha256(open(path, 'rb').read()).hexdigest()

# import zipfile
# path_to_zip_file = "/home/lyvd/python_class/abc.txt.zip"
# zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
# directory_to_extract_to = "/home/lyvd/python_class/storehere"
# zip_ref.extractall(directory_to_extract_to)
# zip_ref.close()

# import glob

# for filename in glob.iglob('storehere/*.pdf'):
#     print(filename)


# import os
# # os.system('/usr/bin/xdg-open /home/user/Examples/case_Contact.pdf')
# os.system('/usr/bin/gnome-open thinkpython.pdf')

# import zipfile
         
# jungle_zip = zipfile.ZipFile('bhk.zip', 'w')
# jungle_zip.write('thinkpython.pdf', compress_type=zipfile.ZIP_DEFLATED)
 
# jungle_zip.close()

# import os
# import zipfile
 
# fantasy_zip = zipfile.ZipFile('tat.zip', 'w')
 
# for folder, subfolders, files in os.walk('/home/lyvd/python_class/storehere'):
 
#     for file in files:
#         if file.endswith('.txt'):
#             fantasy_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), 'C:\\Stories\\Fantasy'), compress_type = zipfile.ZIP_DEFLATED)
 
# fantasy_zip.close()


import os
from shutil import *
import shutil
path = "/home/lyvd/python_class/store1"
storehere = "/home/lyvd/python_class/storehere"
if (os.path.isdir(path))== True:
	shutil.rmtree(path)
os.makedirs(path)

for dirpath,_,filenames in os.walk(storehere):
   for f in filenames:
       abpath = os.path.abspath(os.path.join(dirpath, f))
       shutil.copy(f, path)
