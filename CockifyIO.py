import datetime as dt
from CockifyClasses import *

# Note that Y has to be UpCase dtFormat to allow for ABCD format
def dtToStr(inp, dtFormat = '%Y-%m-%d %H:%M:%S'):
       return dt.datetime.strptime(inp, dtFormat)

def readFile(directory):
	f = open(directory, 'r')
	s = f.read()

	ss = s.split("+")

	prj = ss[0].split("\n")[:-1]

	for r in prj:
		t = r.split(',')
		retPr = Project(t[0], t[1:])
		#retEv = Event()
		print(retPr)

	f.close()