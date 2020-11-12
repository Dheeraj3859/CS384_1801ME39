import os
import re
path = './Subtitles/Game of Thrones'
files = os.listdir(path)
for f in files:
	stri=""
	x=f.split(' - ')
	for c in f:
		if c=='.':
			break
		else:
			stri+=c
	temp=x[1].split('x')
	print(temp)
	
print(len(path))