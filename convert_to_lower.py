# take input of a filename on command line, convert the contents of the file to lowercase.

import sys
f = sys.argv[1]
myfile = open(f).read().split()
for item in myfile:
	print item.lower()
