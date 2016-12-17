import sys
sys.stderr.write('repeater.py: starting\n')
sys.stderr.flush()
tong = 0
while True:
	next_line = sys.stdin.readline()
	if not next_line:
		break
	tong = tong + int(next_line)
	sys.stdout.write(next_line)
	sys.stdout.write("\n")
	sys.stdout.write(str(tong))
	sys.stdout.write("\n")
	sys.stdout.flush()
sys.stderr.write('repeater.py: exiting\n')
sys.stderr.flush()