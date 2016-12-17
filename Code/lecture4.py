import subprocess

# goi mot command don gian ls -l (liet ke file)
# output = subprocess.call(['ls', '-l'])

# # Kiem tra loi khi goi mot process
# error = subprocess.check_call(['ls', '-l'])

# # Truong hop mot loi goi ham sai
# try:
# 	subprocess.check_call(['ls', '-w'])
# except subprocess.CalledProcessError as e:
# 	print("Error: {}".format(e))

# #print("Error code: {} ".format(error))

# # check type
# #print((output))

# # Lay output tra ve
# output = subprocess.check_output(['ls', '-l'])
# print("So luong bytes trong output: {}".format(len(output)))
# print("Output: {}".format(output))
# print("Output type: {}".format(type(output)))

# # Chay nhieu command
# multi_command = subprocess.check_output('ls -l | grep Downloads', shell = True)
# print("Ls with grep: {}".format(multi_command))

# multi_command = subprocess.check_output('mkdir test; cd test; touch test.txt; echo "Hello" > test.txt', shell = True)

# # Giao tiep voi tien trinh thong qua Popen 
# # listfile = subprocess.Popen(['ls', '-l'],
# # stdout=subprocess.PIPE,)
# # stdout_value = listfile.communicate()[0]
# # print("Ouput value: {}".format((stdout_value)))


# # Giao tiep 2 chieu
# # bidirect = subprocess.Popen('ls -l',shell = True,
# # stdin=subprocess.PIPE,
# # stdout=subprocess.PIPE,)
# # command = 'Hello'
# # stdout_value1 = bidirect.communicate(command)
# # print("--Bidriect--")
# # print("Output: {}".format(stdout_value1))

# # Pipelines
# cat = subprocess.Popen(['cat', 'index.txt'],
# stdout=subprocess.PIPE,)

# grep = subprocess.Popen(['grep', '-i', 'mickey'],
# stdin=cat.stdout,
# stdout=subprocess.PIPE,
# )

# end_of_pipe = grep.stdout

# print("Type: {}".format(end_of_pipe))


# for line in end_of_pipe:
# 	print("Line: {}".format(line.strip()))

# print 'One line at a time:'
# proc = subprocess.Popen('python sum_repeater.py',
# shell=True,
# stdin=subprocess.PIPE,
# stdout=subprocess.PIPE,
# )
# for i in range(5):
# 	proc.stdin.write('%d\n' % i)
# 	output = proc.stdout.readline()
# 	print output.rstrip()
# remainder = proc.communicate()[0]
# print remainder


# Loi cu phap
#print("Hello world"

# Ngoai le
# Chia cho so 0
#print("Ngoai le: {}".format(1/0))

# Ten khong duoc dinh nghia
#print("Ten khong duoc dinh nghia: {}".format(4 + name*3))

# Ngoai le ve kieu
print("Ngoai le ve kieu: {}".format())