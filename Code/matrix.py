#!/usr/bin/python2.7

import sys
print sys.argv
if len(sys.argv) == 2:
    print("Hello {0}".format(sys.argv[1]))
else:
    print(sys.stderr.write("Usage:i {0} name\n".format(sys.argv[0])))
