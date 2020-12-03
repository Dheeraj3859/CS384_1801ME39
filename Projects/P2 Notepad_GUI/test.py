text = "th fthis is a sthing"
s = "th"
ind=0
while 1:
	ind = text.search(s,ind,nocase=1,stopindex=END)
	if not ind:
		break
	lastind = '% s+% dc' % (ind, len(s))
	print("lastind=",lastind)
	ind=lastind

